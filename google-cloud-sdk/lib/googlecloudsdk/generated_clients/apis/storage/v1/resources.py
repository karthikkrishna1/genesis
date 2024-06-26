# -*- coding: utf-8 -*- #
# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for Cloud Platform Apis generated from apitools."""

import enum


BASE_URL = 'https://storage.googleapis.com/storage/v1/'
DOCS_URL = 'https://developers.google.com/storage/docs/json_api/'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  ANYWHERECACHES = (
      'anywhereCaches',
      'b/{bucket}/anywhereCaches/{anywhereCacheId}',
      {},
      ['bucket', 'anywhereCacheId'],
      True
  )
  BUCKETACCESSCONTROLS = (
      'bucketAccessControls',
      'b/{bucket}/acl/{entity}',
      {},
      ['bucket', 'entity'],
      True
  )
  BUCKETS = (
      'buckets',
      'b/{bucket}',
      {},
      ['bucket'],
      True
  )
  BUCKETS_OPERATIONS = (
      'buckets.operations',
      'b/{bucket}/operations/{operationId}',
      {},
      ['bucket', 'operationId'],
      True
  )
  DEFAULTOBJECTACCESSCONTROLS = (
      'defaultObjectAccessControls',
      'b/{bucket}/defaultObjectAcl/{entity}',
      {},
      ['bucket', 'entity'],
      True
  )
  FOLDERS = (
      'folders',
      'b/{bucket}/folders/{folder}',
      {},
      ['bucket', 'folder'],
      True
  )
  MANAGEDFOLDERS = (
      'managedFolders',
      'b/{bucket}/managedFolders/{managedFolder}',
      {},
      ['bucket', 'managedFolder'],
      True
  )
  NOTIFICATIONS = (
      'notifications',
      'b/{bucket}/notificationConfigs/{notification}',
      {},
      ['bucket', 'notification'],
      True
  )
  OBJECTACCESSCONTROLS = (
      'objectAccessControls',
      'b/{bucket}/o/{object}/acl/{entity}',
      {},
      ['bucket', 'object', 'entity'],
      True
  )
  OBJECTS = (
      'objects',
      'b/{bucket}/o/{object}',
      {},
      ['bucket', 'object'],
      True
  )
  PROJECTS = (
      'projects',
      'projects/{project}',
      {},
      ['project'],
      True
  )
  PROJECTS_HMACKEYS = (
      'projects.hmacKeys',
      'projects/{projectId}/hmacKeys/{accessId}',
      {},
      ['projectId', 'accessId'],
      True
  )
  PROJECTS_SERVICEACCOUNT = (
      'projects.serviceAccount',
      'projects/{projectId}/serviceAccount',
      {},
      ['projectId'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing
