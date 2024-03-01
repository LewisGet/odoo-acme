# What is this?

This is a odoo plugin that make controller read acme text file.
Its a lazy way to using file authenticate acme without change http server config.

# Default getting start

update the `default_acme_path` in `controllers/regedit.py:7` to your path setting.

# Docker compose

add volumes to `docker-compose.yml`

```
- ./acme:/var/www/public_html
```
