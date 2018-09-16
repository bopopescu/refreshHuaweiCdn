#!/bin/bash

#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#   
#   文件名称：restart.sh
#   创 建 者：xxx
#   邮    箱：xxxxxxx@mujoy.com
#   创建日期：2018年09月15日
#   描    述：
#
#================================================================

/root/.pyenv/versions/3.6.1/bin/uwsgi --reload /var/run/refreshHuaweiCdn.pid
