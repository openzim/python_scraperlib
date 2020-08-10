#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from zimscraperlib.filesystem import get_content_mimetype, get_file_mimetype


def test_file_mimetype(png_image, jpg_image):
    assert get_file_mimetype(png_image) == "image/png"
    assert get_file_mimetype(jpg_image) == "image/jpeg"


def test_content_mimetype(png_image, jpg_image):
    with open(png_image, "rb") as fh:
        assert get_content_mimetype(fh.read(64)) == "image/png"

    with open(jpg_image, "rb") as fh:
        assert get_content_mimetype(fh.read(64)) == "image/jpeg"


def test_mime_overrides(svg_image):
    mime_map = [(svg_image, "image/svg+xml")]
    for fpath, expected_mime in mime_map:
        assert get_file_mimetype(fpath) == expected_mime
        with open(fpath, "rb") as fh:
            assert get_content_mimetype(fh.read(64)) == expected_mime
