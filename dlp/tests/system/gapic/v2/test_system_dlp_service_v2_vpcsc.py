from __future__ import print_function
# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pytest

from google.cloud import dlp_v2
from google.cloud.dlp_v2 import enums
from google.cloud.dlp_v2.proto import dlp_pb2
from google.api_core import exceptions

PROJECT_INSIDE = os.environ.get("PROJECT_ID", None)
PROJECT_OUTSIDE = os.environ.get(
    "GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT", None)
IS_INSIDE_VPCSC = (
    os.environ.get("GOOGLE_CLOUD_TESTS_IN_VPCSC", "false").lower() == "true")


class TestSystemDlpService(object):

  @staticmethod
  def _is_rejected(call):
    try:
      responses = call()
    except exceptions.PermissionDenied as e:
      print("********____:", e.message)
      return e.message == "Request is prohibited by organization's policy"
    except Exception as e:
      print("unexpected error:", e)
      pass
    return False

  @staticmethod
  def _do_test(delayed_inside, delayed_outside):
    if IS_INSIDE_VPCSC:
      assert TestSystemDlpService._is_rejected(delayed_outside)
      assert not (TestSystemDlpService._is_rejected(delayed_inside))
    else:
      assert not (TestSystemDlpService._is_rejected(delayed_outside))
      assert TestSystemDlpService._is_rejected(delayed_inside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_list_deidentify_templates(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.list_deidentify_templates(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.list_deidentify_templates(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_list_dlp_jobs(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.list_dlp_jobs(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.list_dlp_jobs(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_list_job_triggers(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.list_job_triggers(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.list_job_triggers(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_get_job_trigger(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.get_job_trigger(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.get_job_trigger(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_update_stored_info_type(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.update_stored_info_type(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.update_stored_info_type(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_get_stored_info_type(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.get_stored_info_type(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.get_stored_info_type(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_list_stored_info_types(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.list_stored_info_types(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.list_stored_info_types(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)

  @pytest.mark.skipif(
      not IS_INSIDE_VPCSC,
      reason="This test requires a VPCSC and setting GOOGLE_CLOUD_TESTS_IN_VPCSC",
  )
  @pytest.mark.skipif(
      PROJECT_OUTSIDE is None,
      reason="Missing environment variable: GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT",
  )
  def test_delete_stored_info_type(self):
    client = dlp_v2.DlpServiceClient()
    name_inside = client.project_path(PROJECT_INSIDE)
    delayed_inside = lambda: client.delete_stored_info_type(name_inside)
    name_outside = client.project_path(PROJECT_OUTSIDE)
    delayed_outside = lambda: client.delete_stored_info_type(name_outside)
    TestSystemDlpService._do_test(delayed_inside, delayed_outside)
