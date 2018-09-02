# -*- coding: cp936 -*-
import logging


#Ĭ������£�logging����־��ӡ����Ļ����־����ΪWARNING��
#��־�����С��ϵΪ��CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET����ȻҲ�����Լ�������־����

#����־������ļ�

# logging.basicConfig(level=logging.DEBUG,
                # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                # datefmt='%a, %d %b %Y %H:%M:%S',
                # filename='myapp.log',
                # filemode='a') #'w'

#����
logger = logging.getLogger()
filehandler = logging.FileHandler('myapp.log')
formathandler = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
filehandler.setFormatter(formathandler)
logger.addHandler(filehandler)
logger.setLevel(logging.DEBUG)


#�������Ļ
#����һ��StreamHandler����INFO�������ߵ���־��Ϣ��ӡ����׼���󣬲�������ӵ���ǰ����־�������#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

#logging.basicConfig����������:
#filename: ָ����־�ļ���
#filemode: ��file����������ͬ��ָ����־�ļ��Ĵ�ģʽ��'w'��'a'
#format: ָ������ĸ�ʽ�����ݣ�format��������ܶ�������Ϣ����������ʾ:
# %(levelno)s: ��ӡ��־�������ֵ
# %(levelname)s: ��ӡ��־��������
# %(pathname)s: ��ӡ��ǰִ�г����·������ʵ����sys.argv[0]
# %(filename)s: ��ӡ��ǰִ�г�����
# %(funcName)s: ��ӡ��־�ĵ�ǰ����
# %(lineno)d: ��ӡ��־�ĵ�ǰ�к�
# %(asctime)s: ��ӡ��־��ʱ��
# %(thread)d: ��ӡ�߳�ID
# %(threadName)s: ��ӡ�߳�����
# %(process)d: ��ӡ����ID
# %(message)s: ��ӡ��־��Ϣ
#datefmt: ָ��ʱ���ʽ��ͬtime.strftime()
#level: ������־����Ĭ��Ϊlogging.WARNING
#stream: ָ������־�������������ָ�������sys.stderr,sys.stdout�����ļ���Ĭ�������sys.stderr����stream��filenameͬʱָ��ʱ��stream������
