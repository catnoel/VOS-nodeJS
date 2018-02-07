"""Generated client library for ml version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.ml.v1 import ml_v1_messages as messages


class MlV1(base_api.BaseApiClient):
  """Generated client library for service ml version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://ml.googleapis.com/'

  _PACKAGE = u'ml'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'MlV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new ml handle."""
    url = url or self.BASE_URL
    super(MlV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_jobs = self.ProjectsJobsService(self)
    self.projects_models_versions = self.ProjectsModelsVersionsService(self)
    self.projects_models = self.ProjectsModelsService(self)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsJobsService(base_api.BaseApiService):
    """Service class for the projects_jobs resource."""

    _NAME = u'projects_jobs'

    def __init__(self, client):
      super(MlV1.ProjectsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Cancels a running job.

      Args:
        request: (MlProjectsJobsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs/{jobsId}:cancel',
        http_method=u'POST',
        method_id=u'ml.projects.jobs.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'googleCloudMlV1CancelJobRequest',
        request_type_name=u'MlProjectsJobsCancelRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      """Creates a training or a batch prediction job.

      Args:
        request: (MlProjectsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs',
        http_method=u'POST',
        method_id=u'ml.projects.jobs.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/jobs',
        request_field=u'googleCloudMlV1Job',
        request_type_name=u'MlProjectsJobsCreateRequest',
        response_type_name=u'GoogleCloudMlV1Job',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Describes a job.

      Args:
        request: (MlProjectsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs/{jobsId}',
        http_method=u'GET',
        method_id=u'ml.projects.jobs.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsJobsGetRequest',
        response_type_name=u'GoogleCloudMlV1Job',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (MlProjectsJobsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs/{jobsId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'ml.projects.jobs.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'MlProjectsJobsGetIamPolicyRequest',
        response_type_name=u'GoogleIamV1Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the jobs in the project.

      Args:
        request: (MlProjectsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs',
        http_method=u'GET',
        method_id=u'ml.projects.jobs.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/jobs',
        request_field='',
        request_type_name=u'MlProjectsJobsListRequest',
        response_type_name=u'GoogleCloudMlV1ListJobsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a specific job resource.

Currently the only supported fields to update are `labels`.

      Args:
        request: (MlProjectsJobsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Job) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs/{jobsId}',
        http_method=u'PATCH',
        method_id=u'ml.projects.jobs.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'googleCloudMlV1Job',
        request_type_name=u'MlProjectsJobsPatchRequest',
        response_type_name=u'GoogleCloudMlV1Job',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (MlProjectsJobsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs/{jobsId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'ml.projects.jobs.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:setIamPolicy',
        request_field=u'googleIamV1SetIamPolicyRequest',
        request_type_name=u'MlProjectsJobsSetIamPolicyRequest',
        response_type_name=u'GoogleIamV1Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (MlProjectsJobsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/jobs/{jobsId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'ml.projects.jobs.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:testIamPermissions',
        request_field=u'googleIamV1TestIamPermissionsRequest',
        request_type_name=u'MlProjectsJobsTestIamPermissionsRequest',
        response_type_name=u'GoogleIamV1TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsModelsVersionsService(base_api.BaseApiService):
    """Service class for the projects_models_versions resource."""

    _NAME = u'projects_models_versions'

    def __init__(self, client):
      super(MlV1.ProjectsModelsVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a new version of a model from a trained TensorFlow model.

If the version created in the cloud by this call is the first deployed
version of the specified model, it will be made the default version of the
model. When you add a version to a model that already has one or more
versions, the default version does not automatically change. If you want a
new version to be the default, you must call
[projects.models.versions.setDefault](/ml-engine/reference/rest/v1/projects.models.versions/setDefault).

      Args:
        request: (MlProjectsModelsVersionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}/versions',
        http_method=u'POST',
        method_id=u'ml.projects.models.versions.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/versions',
        request_field=u'googleCloudMlV1Version',
        request_type_name=u'MlProjectsModelsVersionsCreateRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a model version.

Each model can have multiple versions deployed and in use at any given
time. Use this method to remove a single version.

Note: You cannot delete the version that is set as the default version
of the model unless it is the only remaining version.

      Args:
        request: (MlProjectsModelsVersionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}/versions/{versionsId}',
        http_method=u'DELETE',
        method_id=u'ml.projects.models.versions.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsModelsVersionsDeleteRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a model version.

Models can have multiple versions. You can call
[projects.models.versions.list](/ml-engine/reference/rest/v1/projects.models.versions/list)
to get the same information that this method returns for all of the
versions of a model.

      Args:
        request: (MlProjectsModelsVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Version) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}/versions/{versionsId}',
        http_method=u'GET',
        method_id=u'ml.projects.models.versions.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsModelsVersionsGetRequest',
        response_type_name=u'GoogleCloudMlV1Version',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Gets basic information about all the versions of a model.

If you expect that a model has a lot of versions, or if you need to handle
only a limited number of results at a time, you can request that the list
be retrieved in batches (called pages):

      Args:
        request: (MlProjectsModelsVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1ListVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}/versions',
        http_method=u'GET',
        method_id=u'ml.projects.models.versions.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/versions',
        request_field='',
        request_type_name=u'MlProjectsModelsVersionsListRequest',
        response_type_name=u'GoogleCloudMlV1ListVersionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates the specified Version resource.

Currently the only supported field to update is `description`.

      Args:
        request: (MlProjectsModelsVersionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}/versions/{versionsId}',
        http_method=u'PATCH',
        method_id=u'ml.projects.models.versions.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'googleCloudMlV1Version',
        request_type_name=u'MlProjectsModelsVersionsPatchRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def SetDefault(self, request, global_params=None):
      """Designates a version to be the default for the model.

The default version is used for prediction requests made against the model
that don't specify a version.

The first version to be created for a model is automatically set as the
default. You must make any subsequent changes to the default version
setting manually using this method.

      Args:
        request: (MlProjectsModelsVersionsSetDefaultRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Version) The response message.
      """
      config = self.GetMethodConfig('SetDefault')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetDefault.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}/versions/{versionsId}:setDefault',
        http_method=u'POST',
        method_id=u'ml.projects.models.versions.setDefault',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:setDefault',
        request_field=u'googleCloudMlV1SetDefaultVersionRequest',
        request_type_name=u'MlProjectsModelsVersionsSetDefaultRequest',
        response_type_name=u'GoogleCloudMlV1Version',
        supports_download=False,
    )

  class ProjectsModelsService(base_api.BaseApiService):
    """Service class for the projects_models resource."""

    _NAME = u'projects_models'

    def __init__(self, client):
      super(MlV1.ProjectsModelsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a model which will later contain one or more versions.

You must add at least one version before you can request predictions from
the model. Add versions by calling
[projects.models.versions.create](/ml-engine/reference/rest/v1/projects.models.versions/create).

      Args:
        request: (MlProjectsModelsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Model) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models',
        http_method=u'POST',
        method_id=u'ml.projects.models.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/models',
        request_field=u'googleCloudMlV1Model',
        request_type_name=u'MlProjectsModelsCreateRequest',
        response_type_name=u'GoogleCloudMlV1Model',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a model.

You can only delete a model if there are no versions in it. You can delete
versions by calling
[projects.models.versions.delete](/ml-engine/reference/rest/v1/projects.models.versions/delete).

      Args:
        request: (MlProjectsModelsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}',
        http_method=u'DELETE',
        method_id=u'ml.projects.models.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsModelsDeleteRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a model, including its name, the description (if.
set), and the default version (if at least one version of the model has
been deployed).

      Args:
        request: (MlProjectsModelsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1Model) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}',
        http_method=u'GET',
        method_id=u'ml.projects.models.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsModelsGetRequest',
        response_type_name=u'GoogleCloudMlV1Model',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (MlProjectsModelsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'ml.projects.models.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'MlProjectsModelsGetIamPolicyRequest',
        response_type_name=u'GoogleIamV1Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the models in a project.

Each project can contain multiple models, and each model can have multiple
versions.

      Args:
        request: (MlProjectsModelsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1ListModelsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models',
        http_method=u'GET',
        method_id=u'ml.projects.models.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/models',
        request_field='',
        request_type_name=u'MlProjectsModelsListRequest',
        response_type_name=u'GoogleCloudMlV1ListModelsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a specific model resource.

Currently the only supported fields to update are `description` and
`default_version.name`.

      Args:
        request: (MlProjectsModelsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}',
        http_method=u'PATCH',
        method_id=u'ml.projects.models.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'googleCloudMlV1Model',
        request_type_name=u'MlProjectsModelsPatchRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (MlProjectsModelsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'ml.projects.models.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:setIamPolicy',
        request_field=u'googleIamV1SetIamPolicyRequest',
        request_type_name=u'MlProjectsModelsSetIamPolicyRequest',
        response_type_name=u'GoogleIamV1Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (MlProjectsModelsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/models/{modelsId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'ml.projects.models.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:testIamPermissions',
        request_field=u'googleIamV1TestIamPermissionsRequest',
        request_type_name=u'MlProjectsModelsTestIamPermissionsRequest',
        response_type_name=u'GoogleIamV1TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = u'projects_operations'

    def __init__(self, client):
      super(MlV1.ProjectsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (MlProjectsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'ml.projects.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field='',
        request_type_name=u'MlProjectsOperationsCancelRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (MlProjectsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'ml.projects.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsOperationsDeleteRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (MlProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'ml.projects.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'MlProjectsOperationsGetRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (MlProjectsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations',
        http_method=u'GET',
        method_id=u'ml.projects.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/operations',
        request_field='',
        request_type_name=u'MlProjectsOperationsListRequest',
        response_type_name=u'GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(MlV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetConfig(self, request, global_params=None):
      """Get the service account information associated with your project. You need.
this information in order to grant the service account persmissions for
the Google Cloud Storage location where you put your model training code
for training the model with Google Cloud Machine Learning.

      Args:
        request: (MlProjectsGetConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudMlV1GetConfigResponse) The response message.
      """
      config = self.GetMethodConfig('GetConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetConfig.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}:getConfig',
        http_method=u'GET',
        method_id=u'ml.projects.getConfig',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:getConfig',
        request_field='',
        request_type_name=u'MlProjectsGetConfigRequest',
        response_type_name=u'GoogleCloudMlV1GetConfigResponse',
        supports_download=False,
    )

    def Predict(self, request, global_params=None):
      """Performs prediction on the data in the request.
Cloud ML Engine implements a custom `predict` verb on top of an HTTP POST
method. For details of the format, see the **guide to the
[predict request format](/ml-engine/docs/v1/predict-request)**.

      Args:
        request: (MlProjectsPredictRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleApiHttpBody) The response message.
      """
      config = self.GetMethodConfig('Predict')
      return self._RunMethod(
          config, request, global_params=global_params)

    Predict.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}:predict',
        http_method=u'POST',
        method_id=u'ml.projects.predict',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:predict',
        request_field=u'googleCloudMlV1PredictRequest',
        request_type_name=u'MlProjectsPredictRequest',
        response_type_name=u'GoogleApiHttpBody',
        supports_download=False,
    )
