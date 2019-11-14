import scrapy
from scrapy.mail import MailSender

class StackoverflowEmailSpider(scrapy.Spider):

    name ='email_notification'

    start_urls = ["https://stackoverflow.com/questions/37109968/how-to-convert-binary-fraction-to-decimal"]


    def parse(self, response):

        answer_flag = response\
            .css("#answers-header > div > h2::text")\
            .re(r'(\d)\s[A-Z][a-z]+')

        if not answer_flag:

            self.logger.info("There are No Answers on this questions yet!")

        else:

            mailer = MailSender(
                                smtphost="smtp.gmail.com",
                                mailfrom="vieraenterprises@gmail.com",
                                smtpuser="vieraenterprises@gmail.com",
                                smtppass="!bHe/e=K",
                                smtpport=587
                        )

            msg_body = "Hi there, \n\nThere are" + answer_flag[0] + \
                        " answers to your question on stackoverflow. " + \
                        "Here's the link:\n" + response.url

            mailer.send(
                        to=["hviera@harmonyanalytics.org"],
                        subject = "Someone responded to your question on your stackoverflow",
                        body=msg_body, cc=["vieraenterprises@gmail.com"]
            )

