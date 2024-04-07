# genesis

WOKE helps you stay woke against the perils of deepfake manipulation. It operates as a secure video-calling service equipped with AI capabilities to detect instances of deepfake impersonation. Seamlessly integrated into the user experience, WOKE utilizes Gemini's AI model to analyze incoming video streams in real-time. Upon detection of any signs of deepfake manipulation, WOKE promptly alerts the user, providing vital warnings and safeguards. Leveraging our model, various frames of the call recipient's face are scrutinized by Gemini, utilizing Google's powerful infrastructure to ascertain conversational authenticity.

WOKE uses a flask backend, connected to a React frontend while utilizing tools like Google Gemini AI and Google Cloud Storage to temporarily store, process, and determine whether the other caller is a deepfake.

