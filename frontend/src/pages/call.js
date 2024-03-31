import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import PhoneDisabledIcon from "@mui/icons-material/PhoneDisabled";
import TextField from "@mui/material/TextField";
import AssignmentIcon from "@mui/icons-material/Assignment";
import PhoneIcon from "@mui/icons-material/Phone";
import React, { useEffect, useRef, useState } from "react";
import { CopyToClipboard } from "react-copy-to-clipboard";
import Peer from "simple-peer";
import io from "socket.io-client";
import axios from "axios";

const socket = io.connect("http://localhost:5000");

function Call() {
  const intervalRef = useRef();
  const [me, setMe] = useState("");
  const [stream, setStream] = useState();
  const [receivingCall, setReceivingCall] = useState(false);
  const [caller, setCaller] = useState("");
  const [callerSignal, setCallerSignal] = useState();
  const [callAccepted, setCallAccepted] = useState(false);
  const [idToCall, setIdToCall] = useState("");
  const [callEnded, setCallEnded] = useState(false);
  const [name, setName] = useState("");
  const myVideo = useRef();
  const userVideo = useRef();
  const connectionRef = useRef();
  const hasVideo = callAccepted && !callEnded && userVideo?.current?.srcObject;

  useEffect(() => {
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: true })
      .then((stream) => {
        setStream(stream);
        myVideo.current.srcObject = stream;
      })
      .catch((error) => console.error("Error accessing media devices:", error));

    socket.on("me", (id) => {
      setMe(id);
    });

    socket.on("callUser", (data) => {
      setReceivingCall(true);
      setCaller(data.from);
      setName(data.name);
      setCallerSignal(data.signal);
    });
    intervalRef.current = setInterval(captureAndSaveImage, 1000);
    return () => {
      // Cleanup interval on component unmount
      clearInterval(intervalRef.current);
    };
  }, []);

  const captureAndSaveImage = () => {
    console.log("trial");
    console.log();
    if (userVideo.current) {
      console.log("hello");
      const track = userVideo.current.srcObject.getVideoTracks()[0];
      console.log(track);
      const imageCapture = new ImageCapture(track);
      console.log(imageCapture);
      imageCapture.grabFrame().then((bitmap) => {
        const canvas = document.createElement("canvas");
        canvas.width = bitmap.width;
        canvas.height = bitmap.height;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(bitmap, 0, 0, bitmap.width, bitmap.height);
        let imageURL = canvas
          .toDataURL("image/png")
          .replace(/^data:image\/(png|jpg);base64,/, "");
        
        // Send the image to the server
        const imagedata = {
          body: imageURL
        };

        axios.post('http://localhost:5000/api/upload', imagedata).then((response) => {
          console.log(response.data);
          const url = {
            body: response.data.replace('https://storage.googleapis.com', 'gs:/')
          }
          axios.post('http://localhost:5000/api/model', url). then((response) => {
            console.log(response.data);
          }).catch((error) => {
            console.log(error)
          })
        }).catch((error) => {
          console.log(error);
        })
        // fetch('http://localhost:5000/api/upload', imagedata).then((response) => {
        //     console.log(response.data);
        // }).catch((error) => {
        //     console.log(error);
        // });

        // axios.post('http://localhost:5000/api/model', url).then((response) => {
        //   console.log(response.data);
        // }).catch((error) => {
        //   console.log(error);
        // });
        axios.get('http://localhost:5000/api/model').then((response) => {
          console.log(response.data);
        }).catch((error) => {
          console.log(error);
        })
      });
    }
  };

  const callUser = (id) => {
    const peer = new Peer({
      initiator: true,
      trickle: false,
      stream: stream,
    });
    peer.on("signal", (data) => {
      socket.emit("callUser", {
        userToCall: id,
        signalData: data,
        from: me,
        name: name,
      });
    });
    peer.on("stream", (stream) => {
      userVideo.current.srcObject = stream;
    });
    socket.on("callAccepted", (signal) => {
      setCallAccepted(true);
      peer.signal(signal);
    });

    connectionRef.current = peer;
  };

  const answerCall = () => {
    setCallAccepted(true);
    const peer = new Peer({
      initiator: false,
      trickle: false,
      stream: stream,
    });
    peer.on("signal", (data) => {
      socket.emit("answerCall", { signal: data, to: caller });
    });
    peer.on("stream", (stream) => {
      userVideo.current.srcObject = stream;
    });

    peer.signal(callerSignal);
    connectionRef.current = peer;
  };

  const leaveCall = () => {
    setCallEnded(true);
    connectionRef.current.destroy();
  };

  return (
    <div className="video-call-container">
      {receivingCall && !callAccepted && (
        <div className="incoming-call">
          <h1>{name} is calling...</h1>
          <Button variant="contained" color="primary" onClick={answerCall}>
            Answer
          </Button>
        </div>
      )}
      <div className="main-video-area">
        <div className="main-video">
          {callAccepted && !callEnded && (
            <video playsInline ref={userVideo} autoPlay className="full-video" />
          )}
          {stream && (
            <video playsInline muted ref={myVideo} autoPlay className="user-video" />
          )}
        </div>
      <div className="controls">
        <TextField
          id="filled-basic"
          label="Name"
          variant="filled"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="text-field"
        />
        <CopyToClipboard text={me}>
          <Button
            variant="contained"
            color="primary"
            startIcon={<AssignmentIcon />}
            className="copy-id-button"
          >
            Copy ID
          </Button>
        </CopyToClipboard>
        <TextField
          id="filled-basic"
          label="ID to call"
          variant="filled"
          value={idToCall}
          onChange={(e) => setIdToCall(e.target.value)}
          className="text-field"
        />
        {callAccepted && !callEnded ? (
          <Button variant="contained" color="secondary" onClick={leaveCall} className="end-call">
            End Call
          </Button>
        ) : (
          <IconButton
            color="primary"
            aria-label="call"
            onClick={() => callUser(idToCall)}
            className="call-button"
          >
            <PhoneIcon />
          </IconButton>
        )}
      </div>
    </div>
    </div>
  );
}

export default Call;