# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import time

from rapid_videocr import get_subtitles
from rapidocr import TextDetector, TextSystem

det_model_path = "resources/models/ch_PP-OCRv2_det_infer.onnx"
cls_model_path = "resources/models/ch_ppocr_mobile_v2.0_cls_infer.onnx"
rec_model_path = "resources/models/ch_mobile_v2.0_rec_infer.onnx"
dict_path = "resources/ppocr_keys_v1.txt"


if __name__ == '__main__':
    s = time.time()

    ocr_system = TextSystem(det_model_path,
                            rec_model_path,
                            cls_model_path,
                            dict_path)
    text_det = TextDetector(det_model_path)

    batch_size = 100
    subtitle_height = None
    is_dilate = True
    error_num = 0.005
    mp4_path = 'assets/test_video/2.mp4'
    output_format = 'all'  # txt, srt, docx, all

    time_start = '00:00:00'
    time_end = '-1'

    result = get_subtitles(mp4_path,
                           ocr_system,
                           batch_size,
                           subtitle_height,
                           time_start=time_start,
                           time_end=time_end,
                           error_num=error_num,
                           output_format=output_format,
                           text_det=text_det,
                           is_dilate=is_dilate)
    print(f'elapse: {time.time() - s}s')
