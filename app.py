#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import app


if __name__ == '__main__':
    # manager.run()
    # print app.url_map
    app.run(debug=True, host="0.0.0.0", port=5000)