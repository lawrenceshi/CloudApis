#导入所有库以及阿里云的sdk
import os
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_openapi import models as open_api_models 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
from datetime import datetime,timezone
import os
from time import sleep
import json
from typing import List
from typing_extensions import runtime
from alibabacloud_cas20200407.client import Client as CasClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cas20200407 import models as cas_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_cas20200407.client import Client as CasClient
from alibabacloud_tea_util.client import Client as TeaCore
from alibabacloud_cdn20180510.client import Client as CdnClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cdn20180510 import models as cdn_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_ecs20140526.client import Client as EcsClient
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


#设置logging
def createLogger(name="Server_Api", log_path="./logs", filename="server.log", debug=False):

    # 确保日志目录存在
    os.makedirs(log_path, exist_ok=True)

    log_file = os.path.join(log_path, filename)

    # 创建 logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 防止重复添加 handler（非常重要）
    if not logger.handlers:

        # 控制台输出
        c_handler = logging.StreamHandler()

        f_handler = logging.FileHandler(log_file, mode='a')
        if debug:
            print("Debug模式已启动-Debug mode is on. Console and file log level set to DEBUG.")
            c_handler.setLevel(logging.DEBUG)
            f_handler.setLevel(logging.DEBUG)
        else:
            c_handler.setLevel(logging.INFO)
            f_handler.setLevel(logging.INFO)

        # 格式
        c_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        f_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger
#定义Server_Api类
class Server_Api():
    #初始化函数
    def __init__(self, debug = False):
        self.create_logger(debug=debug)
        self.logger.info("ServerApi 初始化完成！ServerApi initialized!")
        self.ecs_client = self.create_client_ecs()
        self.logger.debug("ECS Client 初始化完成！ECS Client initialized!")
        self.my_email = "l.k.shi520@gmail.com"
        self.logger.debug("站长邮箱已经设置完成！Email address has been set.")
        self.logger.debug("Server_Api __init__() - Function completed. Bye!")
    #创建日志函数
    def create_logger(self, debug = False):
        if __name__ == "__main__":
            debug = True
        self.logger = createLogger(filename="Server_Api.log", debug=debug)
        self.logger.debug("Logger已初始化完成！Logger initialized successfully.")
        if debug:
            self.logger.debug("Debug模式已启动-Debug mode is on. Console and file log level set to DEBUG.")
        self.logger.info("creat_logger() - Function completed. Bye!")
        return True
    
    def timer(self, time):
        self.logger.debug("timer() - Function started.")
        self.logger.info("我们等待" + str(time) + "秒，请稍后查看！We will wait for " + str(time) + " seconds, please check later!")
        for i in range(time, -1, -1):
            print(f"\rwaiting... " + str(i) + "s",end='', flush=True)
            sleep(1)
        print("")
        self.logger.info("等待结束！Waiting is over!")
        self.logger.debug("timer() - Function completed. Bye!")
    #直接运行函数，包含交互式功能选择
    def Directly_Run(self, debug = False):
        self.logger.debug("Directly_Run() - Function started.")
        if debug != True:
            self.logger.warning("逻辑错误，Debug模式未启动，但是成功进入了直接运行模式-Logical error, Debug mode is not on, but successfully entered Directly_Run mode.")
            return
        print('此为二次封装api，不建议应当在生产环境直接运行！This is a secondary encapsulation API, and should not be run directly in a production environment!')
        self.logger.debug("成功输出提示信息！Successfully output the prompt message!")
        self.logger.warning("该程序被直接执行！进入debug模式！This program is being run directly! Entered debug mode!")
        self.logger.debug("即将要求输入密码！About to ask for password input!")
        if input("请输入调试密码进入：Please enter the debug password to continue: ") == "debug":
            self.logger.info("调试密码(暗号)正确！Debug password is correct!")
            self.logger.debug("即将要求通过二次警告！About to ask for a second warning!")
            input("再次警告！此为二次封装api，不建议应当在生产环境直接运行！此接口仅为调试预留，请按回车键继续...")
            self.logger.debug("用户已经确认警告！User has confirmed the warning!")
            self.logger.debug("即将输出功能选择提示！About to output the function selection prompt!")
            print("1: 更新TSL证书到CDN（Update TLS certificate to CDN）\n2:添加安全组入站规则（Add Security Group Inbound Rule）\n3:移除安全组入站规则（Remove Security Group Inbound Rule）\n4:上传证书至cas \n5:获取所有CDN域名 \n6:同步CAS证书至CDN\n7.发送邮件\n8.退出（Exit）")
            self.logger.debug("成功输出功能选择提示！Successfully output the function selection prompt!\n初始化中...Initializing...")
            Choice = 1
            self.logger.debug("Choice 变量初始化完成！Choice variable initialized!")
            while True:
                self.logger.debug("进入功能选择循环！Entered the function selection loop!")
                self.logger.debug("等待用户输入功能选择！Waiting for user input for function selection!")
                Choice = input("请选择功能（Please select a function）:")
                self.logger.info("用户已选择功能：User has selected function: " + Choice)
                if Choice == "1":
                    self.logger.debug("用户选择了更新CDN证书功能！User selected the Update CDN Certificate function!\n即将执行update_ssl_cdn()函数！About to execute the update_ssl_cdn() function!")
                    self.update_ssl_cdn()
                elif Choice == "2":
                    self.logger.debug("用户选择了添加安全组入站规则功能！User selected the Add Security Group Inbound Rule function!\n即将执行Add_Security_Group()函数！About to execute the Add_Security_Group() function!")
                    self.Add_Security_Group()
                elif Choice == "3":
                    self.logger.debug("用户选择了移除安全组入站规则功能！User selected the Remove Security Group Inbound Rule function!\n即将执行Remove_Security_Group()函数！About to execute the Remove_Security_Group() function!")
                    self.Remove_Security_Group()
                elif Choice == "4":
                    self.logger.debug("用户选择了上传证书至CAS功能！User selected the Upload Certificate to CAS function!\n即将执行upload_cas()函数！About to execute the upload_cas() function!")
                    self.logger.warning("该功能无法直接调用！否则会报错！This function cannot be called directly! Otherwise, it will report an error!")
                    self.Remove_Security_Group()
                elif Choice == "5":
                    self.logger.debug("用户选择了获取所有CDN域名功能！User selected the Get All CDN Domains function!\n即将执行get_cdn_domain()函数！About to execute the get_cdn_domain() function!")
                    self.upload_cas()
                elif Choice == "6":
                    self.logger.debug("用户选择了同步CAS证书至CDN功能！User selected the Sync CAS Certificate to CDN function!\n即将执行Set_Cdn_Domain_SSL_Certificate()函数！About to execute the Set_Cdn_Domain_SSL_Certificate() function!")
                    self.get_cdn_domain()
                elif Choice == "7":
                    self.logger.debug("用户选择了设置CDN域名SSL证书功能！User selected the Set CDN Domain SSL Certificate function!\n即将执行Set_Cdn_Domain_SSL_Certificate()函数！About to execute the Set_Cdn_Domain_SSL_Certificate() function!")
                    self.Set_Cdn_Domain_SSL_Certificate()
                elif Choice == "8":
                    self.logger.debug("用户选择了发送邮件功能！User selected the Send Email function!\n即将执行sent_email()函数！About to execute the sent_email() function!")
                    self.sent_email(Receiver = "l.k.shi520@gmail.com")
                elif Choice == "9":
                    self.logger.debug("用户选择了退出功能！User selected the Exit function!\n即将退出！About to exit!")
                    break
                else:
                    self.logger.warning("用户输入了无效选项！User entered an invalid option!")
                    print("您输入了无效选项！You entered an invalid option!")
        else:
            self.logger.warning("调试密码错误！Debug password is incorrect!")
            print("调试密码错误！Debug password is incorrect!")
            return False
        self.logger.debug("Directly_Run() - Function completed. Bye!")
    #从环境变量导入阿里云Access Key
    def import_aliyun_ak(self):
        try:
            self.logger.debug("即将导入阿里云ak！About to import Aliyun ak!")
            self.Aliyun_Access_Key_ID = os.environ.get("Ali_Key")
            self.logger.debug("阿里云Access Key ID已导入！Aliyun Access Key ID has been imported!")
            self.Aliyun_Access_Key_Secret = os.environ.get("Ali_Secret")
            self.logger.debug("阿里云Access Key Secret已导入！Aliyun Access Key Secret has been imported!")
            self.logger.info("阿里云access key信息已导入！Aliyun access key information has been imported!")
            self.logger.debug("import_aliyun_ak() - Function completed. Bye!")
            return True
        except Exception as e:
            self.logger.error(f"Error occurred while importing Aliyun AK: {e}")
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！在导入阿里云Access Key时发生错误！\n报错信息：{e}\n内部API已触发，请及时留意", subject = "API: 导入阿里云Access Key失败！")
            self.logger.debug("import_aliyun_ak() - Function failed. Bye!")
            return False
    #保留函数
    def import_cloudflare_ak(self):
        self.logger.debug("函数导入获取cloudflare ak！Someone requires to get cloudflare ak!")
        self.logger.warning("由于暂时无cloudflare api使用需求，于是先不配置导入，此函数仅为预留！Due to the current lack of demand for cloudflare API usage, the function for import is not configured for now, just reserved!")
        print("由于暂时无cloudflare api使用需求，于是先不配置导入，此函数仅为预留！Due to the current lack of demand for cloudflare API usage, the function for import is not configured for now, just reserved!")
        return False
    #保留函数
    def import_porkbun_ak(self):
        self.logger.debug("函数导入获取porkbun ak！Someone requires to get porkbun ak!")
        self.logger.warning("由于暂时无porkbun api使用需求，于是先不配置导入，此函数仅为预留！Due to the current lack of demand for porkbun API usage, the function for import is not configured for now, just reserved!")    
        print("由于暂时无porkbun api使用需求，于是先不配置导入，此函数仅为预留！Due to the current lack of demand for porkbun API usage, the function for import is not configured for now, just reserved!")
        return False
    #发送邮件函数
    def sent_email(self,Receiver,minitext = "此为默认内容", header = "Website Owner", subject = '默认内容' ):
        self.logger.debug("函数发送邮件！Someone requires to sent email!")
        self.logger.info("邮件接收者：{}，邮件内容：{}，邮件标题：{}，邮件发送者：{}".format(Receiver,minitext,subject,header))
        sender = os.environ.get("Email_Username")
        self.logger.debug("邮件发送者已设置！Email sender has been set!")
        receivers = Receiver  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.logger.debug("邮件接收者已设置！Email receiver has been set!")
        
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(minitext, 'plain', 'utf-8')
        self.logger.debug("邮件内容已设置！Email content has been set!")
        message['From'] = Header("Lawrence Web", 'utf-8')   # 发送者
        self.logger.debug("邮件发送者已设置！Email sender has been set!")
        message['To'] =  Header(header, 'utf-8')        # 接收者
        self.logger.debug("邮件接收者已设置！Email receiver has been set!")
        
        message['Subject'] = Header(subject, 'utf-8')
        self.logger.debug("邮件标题已设置！Email subject has been set!")
        self.logger.debug("即将发送邮件！About to sent email!")
        try:
            self.logger.debug("已进入try函数，即将开始发送邮件！About to start sending email!")
            smtpObj = os.environ.get("Email_Server")
            self.logger.debug("邮件服务器已导入！Email server has been set!")
            smtpObj = smtplib.SMTP(smtpObj, os.environ.get("Email_Port"))
            self.logger.debug("邮件服务器端口已导入！Email server port has been set!")
            smtpObj.starttls()
            self.logger.debug("邮件服务器已启动TLS！TLS has been started!")
            smtpObj.login(sender, os.environ.get("Email_Password"))
            self.logger.debug("邮件服务器登录成功！Email server login successful!")
            smtpObj.sendmail(sender, receivers, message.as_string())
            self.logger.info("邮件发送成功！Email sent successfully!")
            self.logger.debug("sent_email() - Function completed. Bye!")
            return True
        except smtplib.SMTPException as error:
            self.logger.error("Error: 无法发送邮件！Error: Unable to send email!" + str(error))
            self.logger.debug("sent_email() - Function completed. Bye!")
            return False
    #创建客户端链接
    def create_client_cas(self):
        self.logger.debug("函数创建CAS客户端！Someone requires to create CAS client!")
        """
        createClient  创建客户端
        """
        self.logger.debug("即将链接阿里云CAS服务！About to connect to Aliyun CAS service!")
        config = open_api_models.Config()
        self.logger.debug("已经创立链接配置对象！Config object has been created!")
        # 您账号所属的AccessKey ID
        config.access_key_id = self.Aliyun_Access_Key_ID
        self.logger.debug("阿里云Access Key ID已设置！Aliyun Access Key ID has been set!")
        # 您账号所属的AccessKey Secret
        config.access_key_secret = self.Aliyun_Access_Key_Secret
        self.logger.debug("阿里云Access Key Secret已设置！Aliyun Access Key Secret has been set!")
        config.endpoint = 'cas.aliyuncs.com'
        self.logger.debug("已经配置访问url！Endpoint has been configured!")
        self.logger.debug("阿里云CAS服务链接已创建！Aliyun CAS service client has been created!")
        self.logger.info("create_client_cas() - Function completed. Bye!")
        return CasClient(config)
    #创建客户端链接
    def create_client_cdn(self) -> CdnClient:
        """
        createClient  创建客户端
        """
        self.logger.debug("函数创建CDN客户端！Someone requires to create CDN client!")
        config = open_api_models.Config()
        self.logger.debug("已经创立链接配置对象！Config object has been created!")
        # 导入账户AccessKey ID
        config.access_key_id = self.Aliyun_Access_Key_ID
        self.logger.debug("阿里云Access Key ID已设置！Aliyun Access Key ID has been set!")
        # 导入账户AccessKey Secret
        config.access_key_secret = self.Aliyun_Access_Key_Secret
        self.logger.debug("阿里云Access Key Secret已设置！Aliyun Access Key Secret has been set!")
        config.endpoint = f'cdn.aliyuncs.com'
        self.logger.debug("已经配置访问url！Endpoint has been configured!")
        self.logger.debug("阿里云CDN服务链接已创建！Aliyun CDN service client has been created!")
        self.logger.info("create_client_cdn() - Function completed. Bye!")
        return CdnClient(config)
    #创建客户端链接
    def create_client_ecs(self) -> EcsClient:
        self.logger.debug("函数创建ECS客户端！Someone requires to create ECS client!")
        self.logger.debug("即将访问函数import_aliyun_ak()以导入阿里云Access Key！About to access the function import_aliyun_ak() to import Aliyun Access Key!")
        self.import_aliyun_ak()
        self.logger.debug("阿里云Access Key已导入！Aliyun Access Key has been imported!")
        config = open_api_models.Config()
        self.logger.debug("已经创立链接配置对象！Config object has been created!")
        # 您的AccessKey ID
        config.access_key_id = self.Aliyun_Access_Key_ID
        self.logger.debug("阿里云Access Key ID已设置！Aliyun Access Key ID has been set!")
        # 您的AccessKey Secret
        config.access_key_secret = self.Aliyun_Access_Key_Secret
        self.logger.debug("阿里云Access Key Secret已设置！Aliyun Access Key Secret has been set!")
        # 您的可用区ID
        config.region_id = "cn-shanghai"
        self.logger.debug("已配置地域信息！Region information has been configured!")
        self.logger.debug("阿里云ECS服务链接已创建！Aliyun ECS service client has been created!")
        self.logger.info("create_client_ecs() - Function completed. Bye!")
        return EcsClient(config)
    #上传证书至CAS
    def aliyun_upload_user_certificate_to_cas(self,
        client: CasClient,
        name: str = None,
        cert: str = None,
        key: str = None,
        encrypt_cert=None,
        encrypt_private_key=None,
        sign_cert=None,
        sign_private_key=None
    ) -> cas_models.UploadUserCertificateResponse:
        self.logger.debug("aliyun_upload_user_certificate_to_cas() - Function started. Hello!")
        self.logger.info("正在上传证书至CAS！Uploading certificate to CAS!")
        self.logger.debug("名称：%s; 证书：%s;", name, cert,)
        try:
            request = cas_models.UploadUserCertificateRequest()
            self.logger.debug("已经创建请求对象！Request object has been created!")
            request.name = name
            self.logger.debug("请求对象名称已设置！Request object name has been set!")
            request.cert = cert
            self.logger.debug("请求对象证书内容已设置！Request object certificate content has been set!")
            request.key = key
            self.logger.debug("请求对象私钥内容已设置！Request object private key content has been set!")
            request.encrypt_cert = encrypt_cert
            self.logger.debug("请求对象加密证书内容已设置！Request object encrypt certificate content has been set!")
            request.encrypt_private_key = encrypt_private_key
            self.logger.debug("请求对象加密私钥内容已设置！Request object encrypt private key content has been set!")
            request.encrypt_private_key = encrypt_private_key
            self.logger.debug("请求对象加密私钥内容已设置！Request object encrypt private key content has been set!")
            request.sign_cert = sign_cert
            self.logger.debug("请求对象签名证书内容已设置！Request object sign certificate content has been set!")
            request.sign_private_key = sign_private_key
            self.logger.debug("请求对象签名私钥内容已设置！Request object sign private key content has been set!")
            response = client.upload_user_certificate(request)
            self.logger.info("已经收到响应！Response has been received!")
            result = json.loads(UtilClient.to_jsonstring(TeaCore.to_map(response.body)))
            self.logger.debug("响应内容已转换为字典！Response content has been converted to dictionary!")
            self.logger.info("响应内容：%s", result)
            self.cert_id = result.get("CertId")
            self.logger.info("证书ID：%s", self.cert_id)
        except Exception as error:
            self.logger.error("上传证书至CAS发生错误！Error occurred while uploading certificate to CAS!")
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！在上传证书至CAS时发生错误！\n报错信息：{error}\n内部API已触发，请及时留意", subject = "API: 上传证书至CAS失败！")
            self.logger.error(error.message)
            return None
        return True
    #获取所有CDN域名
    def aliyun_get_all_domains(self,
        args = None,
    ) -> None:
        self.logger.debug("aliyun_get_all_domains() - Function started. Hello!")
        client = self.cdn_client
        self.logger.debug("已经获取CDN客户端！CDN client has been obtained!")
        describe_user_domains_request = cdn_models.DescribeUserDomainsRequest()
        self.logger.debug("已经创建请求对象！Request object has been created!")
        runtime = util_models.RuntimeOptions()
        self.logger.debug("即将发送请求以获取CDN域名列表！About to send request to get CDN domain list!")
        self.logger.info("正在获取CDN域名列表！Getting CDN domain list!")
        try:
            self.logger.debug("已进入try函数，即将开始获取CDN域名列表！About to start getting CDN domain list!")
            resp = client.describe_user_domains_with_options(describe_user_domains_request, runtime)
            self.logger.info("CDN域名列表已获取！CDN domain list has been obtained!")
            data = TeaCore.to_map(resp)
            self.logger.debug("响应内容已转换为字典！Response content has been converted to dictionary!")
            self.logger.info("响应内容：%s", data)

            self.Domain_List = [
                d.get("DomainName")
                for d in data.get("body", {})
                            .get("Domains", {})
                            .get("PageData", [])
            ]
            self.logger.info("CDN域名列表：%s", self.Domain_List)
            self.logger.debug("aliyun_get_all_domains() - Function completed. Bye!")
            return True
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            self.logger.error("获取CDN域名列表时发生错误：%s", error)
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！在获取CDN域名列表时发生错误！\n报错信息：{error}\n内部API已触发，请及时留意", subject = "API: 获取CDN域名列表失败！")
            self.logger.debug("aliyun_get_all_domains() - Function completed with error. Bye!")
            return False
    #设置CDN域名SSL证书
    def aliyun_set_domain_server_certificate(
        self,
        client: CdnClient,
        domain_name: str,
        cert_type='cas',
        server_certificate_status: str = "on",
        cert_name: str = None,
        sslprotocol = "on",
        certId: str = "",

    ) -> None:
        self.logger.debug("aliyun_set_domain_server_certificate() - Function started. Hello!")
        """
        SetDomainServerCertificate  设置加速域名的证书信息
        """
        self.logger.info("正在设置CDN域名SSL证书！Setting CDN domain SSL certificate!")
        self.logger.debug("域名：%s; 证书类型：%s; 证书状态：%s; 证书名称：%s; SSL协议开启状态：%s; 证书ID：%s;", domain_name, cert_type, server_certificate_status, cert_name, sslprotocol, certId)
        request = cdn_models.SetCdnDomainSSLCertificateRequest()
        self.logger.debug("已经创建请求对象！Request object has been created!")
        request.domain_name = domain_name
        self.logger.debug("请求对象域名已设置！Request object domain name has been set!")
        request.server_certificate_status = server_certificate_status
        self.logger.debug("请求对象证书状态已设置！Request object certificate status has been set!")
        request.cert_name = cert_name
        self.logger.debug("请求对象证书名称已设置！Request object certificate name has been set!")
        request.sslprotocol = sslprotocol
        self.logger.debug("请求对象SSL协议开启状态已设置！Request object SSL protocol status has been set!")
        request.cert_id = certId
        self.logger.debug("请求对象证书ID已设置！Request object certificate ID has been set!")
        request.certType = cert_type
        self.logger.debug("请求对象证书类型已设置！Request object certificate type has been set!")
        request.cert_region = "cn-hangzhou"
        self.logger.debug("请求对象证书所属地域已设置！Request object certificate region has been set!")
        self.logger.debug("即将发送请求以设置CDN域名SSL证书！About to send request to set CDN domain SSL certificate!")
        try:
            self.logger.debug("已进入try函数，即将开始设置CDN域名SSL证书！About to start setting CDN domain SSL certificate!")
            runtime = util_models.RuntimeOptions()
            self.logger.debug("Runtime options object has been created!")
            self.logger.info("正在设置CDN域名SSL证书！Setting CDN domain SSL certificate!")
            response = client.set_cdn_domain_sslcertificate_with_options(
                request,
                runtime)
            self.logger.info("CDN域名SSL证书已设置！CDN domain SSL certificate has been set!")
            self.logger.info(TeaCore.to_map(response.body))
            self.logger.debug("aliyun_set_domain_server_certificate() - Function completed. Bye!")
            return True
        except Exception as error:
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！在设置CDN域名SSL证书时发生错误！\n报错信息：{error}\n内部API已触发，请及时留意\n域名：{domain_name}\n证书类型：{cert_type}\n证书状态：{server_certificate_status}\n证书名称：{cert_name}\nSSL协议开启状态：{sslprotocol}\n证书ID：{certId}", subject = "API: 设置CDN域名SSL证书失败！")
            self.logger.error("设置CDN域名SSL证书时发生错误：%s", error)
            return False
    #移除安全组入站规则
    def Remove_Security_Group(
        self,
        security_group_id = 'sg-uf605fsdfsxyynnz079s',
        region = 'cn-shanghai',
        permissions_0_policy='accept',
        permissions_0_priority='99',
        permissions_0_ip_protocol='TCP',
        permissions_0_source_cidr_ip='0.0.0.0/0',
        permissions_0_port_range='443/443',
        permissions_0_description="Remove Security Group",
        permissions_1_policy='accept',
        permissions_1_priority='99',
        permissions_1_ip_protocol='TCP',
        permissions_1_source_cidr_ip='0.0.0.0/0',
        permissions_1_port_range='80/80',
        permissions_1_description='HTTP-01 verify',
    ) -> None:
        self.logger.debug("Remove_Security_Group() - Function started. Hello!")

        client = self.ecs_client
        self.logger.debug("已经获取ECS客户端！ECS client has been obtained!")

        req = ecs_20140526_models.RevokeSecurityGroupRequest()
        self.logger.debug("已经创建请求对象！Request object has been created!")

        req.region_id = region
        self.logger.debug("请求对象地域已设置！Request object region has been set!")
        req.security_group_id = security_group_id
        self.logger.debug("请求对象安全组ID已设置！Request object security group ID has been set!")

        permissions_0 = ecs_20140526_models.RevokeSecurityGroupRequestPermissions()
        permissions_0.policy = permissions_0_policy
        permissions_0.priority = permissions_0_priority
        permissions_0.ip_protocol = permissions_0_ip_protocol
        permissions_0.source_cidr_ip = permissions_0_source_cidr_ip
        permissions_0.port_range = permissions_0_port_range
        permissions_0.description = permissions_0_description

        permissions_1 = ecs_20140526_models.RevokeSecurityGroupRequestPermissions()
        permissions_1.policy = permissions_1_policy
        permissions_1.priority = permissions_1_priority
        permissions_1.ip_protocol = permissions_1_ip_protocol
        permissions_1.source_cidr_ip = permissions_1_source_cidr_ip
        permissions_1.port_range = permissions_1_port_range
        permissions_1.description = permissions_1_description
        self.logger.debug("请求对象权限已设置！Request object permissions have been set!")

        req.permissions = [
            permissions_0,
            permissions_1
        ]
        self.logger.debug("请求对象权限列表已设置！Request object permissions list has been set!")

        runtime = util_models.RuntimeOptions()
        self.logger.debug("Runtime options object has been created!")

        try:
            client.revoke_security_group_with_options(req, runtime)
            self.logger.info("安全组入站规则已成功移除！Security group inbound rules have been successfully removed!")
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！您的安全组入站规则已成功移除！\n内部API已触发，请及时留意\n安全组ID:\n{security_group_id}\n入站规则列表:\n{[permissions_0, permissions_1]}", subject = "API: 安全组入站规则移除成功！")
            self.logger.debug("Remove_Security_Group() - Function completed. Bye!")

            return True
        except Exception as error:
            self.logger.error("移除安全组入站规则时发生错误：%s", error)
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！您的安全组入站规则移除失败！\n报错信息：{error}\n内部API已触发，请及时留意\n安全组ID:\n{security_group_id}\n入站规则列表:\n{[permissions_0, permissions_1]}", subject = "API: 安全组入站规则移除失败！")
            self.logger.debug("Remove_Security_Group() - Function failed. Bye!")
            return False
    def Add_Security_Group(
        self,
        security_group_id = 'sg-uf605fsdfsxyynnz079s',
        region = 'cn-shanghai',
        permissions_0_policy='accept',
        permissions_0_priority='99',
        permissions_0_ip_protocol='TCP',
        permissions_0_source_cidr_ip='0.0.0.0/0',
        permissions_0_port_range='80/80',
        permissions_0_description='HTTP-01 verify',
        permissions_1_policy='accept',
        permissions_1_priority='99',
        permissions_1_ip_protocol='TCP',
        permissions_1_source_cidr_ip='::/0',
        permissions_1_port_range='80/80',
        permissions_1_description='HTTP-01 verify',
    ) -> None:
        self.logger.debug("Add_Security_Group() - Function started. Hello!")

        client = self.ecs_client
        self.logger.debug("已经获取ECS客户端！ECS client has been obtained!")

        req = ecs_20140526_models.AuthorizeSecurityGroupRequest()
        self.logger.debug("已经创建请求对象！Request object has been created!")
        req.region_id = region
        self.logger.debug("请求对象地域已设置！Request object region has been set!")
        req.security_group_id = security_group_id
        self.logger.debug("请求对象安全组ID已设置！Request object security group ID has been set!")

        permissions_0 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions()
        permissions_0.policy = permissions_0_policy
        permissions_0.priority = permissions_0_priority
        permissions_0.ip_protocol = permissions_0_ip_protocol
        permissions_0.source_cidr_ip = permissions_0_source_cidr_ip
        permissions_0.port_range = permissions_0_port_range
        permissions_0.description = permissions_0_description

        permissions_1 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions()
        permissions_1.policy = permissions_1_policy
        permissions_1.priority = permissions_1_priority
        permissions_1.ip_protocol = permissions_1_ip_protocol
        permissions_1.ipv_6source_cidr_ip = permissions_1_source_cidr_ip
        permissions_1.port_range = permissions_1_port_range
        permissions_1.description = permissions_1_description
        self.logger.debug("请求对象权限已设置！Request object permissions have been set!")

        req.permissions = [permissions_0, permissions_1]
        self.logger.debug("请求对象权限列表已设置！Request object permissions list has been set!")
        runtime = util_models.RuntimeOptions()
        self.logger.debug("Runtime options object has been created!")

        try:
            client.authorize_security_group_with_options(req, runtime)
            self.logger.info("安全组入站规则已成功更新！Security group inbound rules have been successfully updated!")
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！您的安全组入站规则已成功更新至阿里云ECS！\n内部API已触发，请及时留意\n安全组ID:\n{security_group_id}\n入站规则列表:\n{[permissions_0, permissions_1]}", subject = "API: 安全组入站规则更新成功！")
            self.logger.debug("Add_Security_Group() - Function completed. Bye!")
            return True
        except Exception as error:
            self.logger.error("更新安全组入站规则时发生错误：%s", error)
            self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！您的安全组入站规则更新失败！\n报错信息：{error}\n内部API已触发，请及时留意\n安全组ID:\n{security_group_id}\n入站规则列表:\n{[permissions_0, permissions_1]}", subject = "API: 安全组入站规则更新失败！")
            self.logger.debug("Add_Security_Group() - Function failed. Bye!")
            return False
        

    def update_ssl_cdn(self):
        self.logger.debug("update_ssl_cdn() - Function started. Hello!")

        self.logger.debug("即将访问函数import_aliyun_ak()以导入阿里云Access Key！About to access the function import_aliyun_ak() to import Aliyun Access Key!")
        self.import_aliyun_ak()
        self.logger.info("函数执行完成")


        self.name = "autoupload-cert-prod-" + str(datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
        self.logger.debug("证书名称已设置！Certificate name has been set!")
        cert_path, key_path = ("/server/tls_certs/certs/cert.pem", "/server/tls_certs/certs/key.pem")
        self.logger.debug("证书路径已设置！Certificate paths have been set!")
        with open(cert_path, "rb") as f:
            self.logger.debug("正在读取证书文件！Reading certificate file!")
            cert_data = f.read()
            self.logger.debug("证书文件已读取！Certificate file has been read!")
        with open(key_path, "rb") as f:
            self.logger.debug("正在读取私钥文件！Reading private key file!")
            key_data = f.read()
            self.logger.debug("私钥文件已读取！Private key file has been read!")
        cert_data = cert_data.decode("utf-8")
        self.logger.debug("证书内容已解码！Certificate content has been decoded!")
        key_data = key_data.decode("utf-8")
        self.logger.debug("私钥内容已解码！Private key content has been decoded!")
        self.cdn_client = self.create_client_cdn()
        self.logger.debug("CDN客户端已创建！CDN client has been created!")
        cas_client = self.create_client_cas()
        self.logger.debug("CAS客户端已创建！CAS client has been created!")
        self.aliyun_upload_user_certificate_to_cas(client = cas_client, name = self.name, cert = cert_data, key = key_data)
        self.logger.debug("证书已上传至CAS！Certificate has been uploaded to CAS!")
        self.aliyun_get_all_domains()
        self.logger.debug("CDN域名列表已获取！CDN domain list has been obtained!")
        for i in self.Domain_List:
            self.logger.debug("正在设置CDN域名SSL证书！Setting CDN domain SSL certificate for domain: %s", i)
            self.aliyun_set_domain_server_certificate(
                client=self.cdn_client,
                domain_name=i,
                server_certificate_status="on",
                cert_name=self.name,
                sslprotocol="on",
                certId=self.cert_id

            )
            self.logger.info("CDN域名%s的SSL证书已设置！CDN domain %s SSL certificate has been set!", i, i)
            self.logger.info("休息5秒钟以避免请求过快！Sleeping for 2 seconds to avoid too fast requests!")
            self.timer(5)
        self.logger.info("所有CDN域名的SSL证书已设置完成！All CDN domains' SSL certificates have been set!")
        self.sent_email(Receiver = self.my_email, minitext = f"亲爱的站长,\n我是您的脚本！您的CDN SSL证书已成功更新至阿里云CDN！\n内部API已触发，请及时留意\n域名列表:\n{self.Domain_List}\n您的证书公钥：\n"+ cert_data, subject = "API: CDN SSL证书更新成功！")

if __name__ == "__main__":
    
    Server_Api().Directly_Run(debug = True)
