#!/bin/bash
# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

echo "=============================================================================================================="
echo "Please run the script as: "
echo "bash scripts/run_standalone_eval_gpu.sh [DATASET] [CHECKPOINT] [CONFIG_PATH]"
echo "for example: bash run_standalone_eval_gpu.sh /path/to/data/ /path/to/checkpoint/ /path/to/config/"
echo "=============================================================================================================="
python eval.py --data_path=$1 --checkpoint_file_path=$2 --config_path=$3 > eval.log  2>&1 &
