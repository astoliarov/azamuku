# coding: utf-8

import os
import multiprocessing

_port = os.getenv('AZAMUKU_PORT', 5000)
_workers = int(os.getenv('AZAMUKU_HTTP_WORKERS', multiprocessing.cpu_count() * 2 + 1))

bind = f"0.0.0.0:{_port}"
backlog = 2048

workers = _workers

accesslog = '-'
errlog = '-'
