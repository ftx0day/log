import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'log.settings'

if __name__ == '__main__':
    send_mail(
        'From MELODY’s test email',
        '本内容为测试使用，请勿回复，注意：请勿回复。',
        'fweiwx@163.com',
        ['278416076@qq.com'],
    )