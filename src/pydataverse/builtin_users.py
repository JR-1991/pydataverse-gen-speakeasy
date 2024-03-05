"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from pydataverse import utils
from pydataverse._hooks import HookContext
from pydataverse.models import errors, operations
from typing import Optional

class BuiltinUsers:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def post_api_v1_builtin_users(self, key: Optional[str] = None, password: Optional[str] = None, send_email_notification: Optional[bool] = None) -> operations.PostAPIV1BuiltinUsersResponse:
        hook_ctx = HookContext(operation_id='post_/api/v1/builtin-users', oauth2_scopes=[], security_source=None)
        request = operations.PostAPIV1BuiltinUsersRequest(
            key=key,
            password=password,
            send_email_notification=send_email_notification,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/v1/builtin-users'
        headers = {}
        query_params = utils.get_query_params(operations.PostAPIV1BuiltinUsersRequest, request)
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostAPIV1BuiltinUsersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_api_v1_builtin_users_password_key_(self, key: str, password: str) -> operations.PostAPIV1BuiltinUsersPasswordKeyResponse:
        hook_ctx = HookContext(operation_id='post_/api/v1/builtin-users/{password}/{key}', oauth2_scopes=[], security_source=None)
        request = operations.PostAPIV1BuiltinUsersPasswordKeyRequest(
            key=key,
            password=password,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostAPIV1BuiltinUsersPasswordKeyRequest, base_url, '/api/v1/builtin-users/{password}/{key}', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostAPIV1BuiltinUsersPasswordKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_api_v1_builtin_users_password_key_send_email_notification_(self, key: str, password: str, send_email_notification: bool) -> operations.PostAPIV1BuiltinUsersPasswordKeySendEmailNotificationResponse:
        hook_ctx = HookContext(operation_id='post_/api/v1/builtin-users/{password}/{key}/{sendEmailNotification}', oauth2_scopes=[], security_source=None)
        request = operations.PostAPIV1BuiltinUsersPasswordKeySendEmailNotificationRequest(
            key=key,
            password=password,
            send_email_notification=send_email_notification,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostAPIV1BuiltinUsersPasswordKeySendEmailNotificationRequest, base_url, '/api/v1/builtin-users/{password}/{key}/{sendEmailNotification}', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostAPIV1BuiltinUsersPasswordKeySendEmailNotificationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_api_v1_builtin_users_username_api_token(self, username: str, password: Optional[str] = None) -> operations.GetAPIV1BuiltinUsersUsernameAPITokenResponse:
        hook_ctx = HookContext(operation_id='get_/api/v1/builtin-users/{username}/api-token', oauth2_scopes=[], security_source=None)
        request = operations.GetAPIV1BuiltinUsersUsernameAPITokenRequest(
            username=username,
            password=password,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAPIV1BuiltinUsersUsernameAPITokenRequest, base_url, '/api/v1/builtin-users/{username}/api-token', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAPIV1BuiltinUsersUsernameAPITokenRequest, request)
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetAPIV1BuiltinUsersUsernameAPITokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    