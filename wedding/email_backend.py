"""
Custom email backend that forces IPv4 for the SMTP connection.

Railway containers frequently lack a working outbound IPv6 route, so Python's
default behaviour of trying Gmail's IPv6 address first fails with
"[Errno 101] Network is unreachable". We temporarily restrict name resolution
to IPv4 (AF_INET) while the SMTP connection is being opened, then restore the
original resolver.
"""
import socket

from django.core.mail.backends.smtp import EmailBackend as SMTPEmailBackend

_original_getaddrinfo = socket.getaddrinfo


def _ipv4_only_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    return _original_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)


class IPv4EmailBackend(SMTPEmailBackend):
    def open(self):
        socket.getaddrinfo = _ipv4_only_getaddrinfo
        try:
            return super().open()
        finally:
            socket.getaddrinfo = _original_getaddrinfo
