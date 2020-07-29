<h2 dir='rtl' align='right'>الاساسيات في اختبار الاختراق  </h2>

<h3 dir='rtl' align='right'> 🧪 بيئة مختبرات اختبار الاختراق "PT" و اصطياد الثغرات "BugBounty"</h3>

## <h3 dir='rtl' align='right'>📚 جدول المحتويات  </h3>

  - [<p dir='rtl' align='right'>🔘 تقارير المكافآت من منصات مختلفة </p>](#web-pentest)
  - [<p dir='rtl' align='right'>🔘 دورة أمان الويب من ستانفورد ( Stanford CS253 Web Security) </p>](#Stanford-CS-253-Web-Security) 
  - [<p dir='rtl' align='right'>🔘 أساسيات بروتوكول HTTP </p>](#HTTP-)
  - [<p dir='rtl' align='right'>🔘 أساسيات الشبكات‪  (Foundations of Networking )‬ </p>](#Network-)
  - [<p dir='rtl' align='right'>🔘 البرمجة</p>](#Programming-)
  - [<p dir='rtl' align='right'>🔘أساسيات الحوسبة Computing Fundamentals </p>](#Computing-Fundamentals)
  - [<p dir='rtl' align='right'>🔘اتممت اختبار الاختراق</p>](#Automation)
  
  
### [<p dir='rtl' align='right'> 📖 تقارير المكافآت من منصات مختلفة </p>](#)
    
- [<p dir='rtl' align='right'> نصائح البداية في مجال اختبار الاختراق واصطياد الثغرات</p>](#)
- [<p dir='rtl' align='right'>🔽 اكتشاف ثغرات XSS</p>](#)
  - [<p dir='rtl' align='right'> ◀️ ثغرة XSS DOM</p>](#)
  - [<p dir='rtl' align='right'> ◀️ ثغرة XSS Stored </p>](#)
- [<p dir='rtl' align='right'>ثغرة SSRF</p>](#)
- [<p dir='rtl' align='right'>اكتشاف الثغرات</p>](#)
- [<p dir='rtl' align='right'>ثغرات مصادقة الحسابات وتخطيها</p>](#)
- [<p dir='rtl' align='right'>ثغرات حقن الاستعلامات SQL</p>](#)
- [<p dir='rtl' align='right'>ثغرة HTTP Desync</p>](#)
- [<p dir='rtl' align='right'>ثغرات رفع الملفات</p>](#)
- [<p dir='rtl' align='right'>ثغرات IDOR </p>](#)
- [<p dir='rtl' align='right'>ثغرات RCE </p>](#)
- [<p dir='rtl' align='right'>الطرق الصحيحة لعمليات الفحص</p>](#)
- [<p dir='rtl' align='right'>ثغرات API </p>](#)
- [<p dir='rtl' align='right'>ثغرات GraphQL </p>](#)

<h4 dir='rtl' align='right'>▪️  نصائح البداية في مجال اختبار الاختراق واصطياد الثغرات </h4>

- [<p dir='rtl' align='right'>🔗 اسئلة و اجوبة عن اصطياد الثغرات من احد مشاهير اكتشاف الثغرات</p>](http://blog.oath.ninja/basic-bug-bounty-faq/)
- [<p dir='rtl' align='right'>🔗 دليل شامل للبدء في مجال اختبار الاختراق</p>](https://www.ceos3c.com/hacking/getting-started-cyber-security-complete-guide/)
- [<p dir='rtl' align='right'>🔗 كيف تقوم باعداد خادم SSH لاستخدامة كمنصة لصطياد الثغرات</p>](https://medium.com/@c0ldbr3w/how-to-set-up-certificate-based-ssh-for-bug-hunting-bonus-ef4af95fca05)
- [<p dir='rtl' align='right'>🔗 دليل استخدام منصة قوقل لثغرات XSS </p>](https://blog.bentkowski.info/2018/06/xss-in-google-colaboratory-csp-bypass.html)
- [<p dir='rtl' align='right'>🔗 نصائح وارشادات عامة في اختبار الاختراق</p>](https://blog.intigriti.com/2020/04/29/bug-business-3-zseanos-notes-on-hacking-mentoring/)
- [<p dir='rtl' align='right'>🔗 رحلتي في اصطياد الثغرات</p>](https://www.youtube.com/watch?v=ug7FzoByLFc)

<h4 dir='rtl' align='right'>▪️  اكتشاف ثغرات XSS </h4>

- [<p dir='rtl' align='right'>🔗 تقرير عن ايجاد ثغرة XSS في موقع قوقل</p>](https://www.youtube.com/watch?v=lG7U3fuNw3A)
- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن ايجاد ثغرة في منصة تسلا وربح 10,000دولار</p>](https://samcurry.net/cracking-my-windshield-and-earning-10000-on-the-tesla-bug-bounty-program/)
- [<p dir='rtl' align='right'>🔗 تقرير يتكلم يتحدث عن طرق جديدة لاكتشاف ثغرات XSS </p>](https://medium.com/bugbountywriteup/effortlessly-finding-cross-site-script-inclusion-xssi-jsonp-for-bug-bounty-38ae0b9e5c8a)
- [<p dir='rtl' align='right'>🔗 تقرير يتكلم عن محاولة استغلال ثغرة XSS للحصول على RCE </p>](https://leucosite.com/Edge-Chromium-EoP-RCE/)
- [<p dir='rtl' align='right'>🔗 تقريرعن مكافة لثغرة Reflected XSS  </p>](https://hackerone.com/reports/824433)
- [<p dir='rtl' align='right'>🔗  تقرير اخر يتحدث عن استغلال ثغرات XSS في منصات قوقل</p>](https://pethuraj.com/blog/google-bug-bounty-writeup/)
- [<p dir='rtl' align='right'>🔗 فيديو يشرح حلول متعددة لتحديات منصة مكافة الثغرات Intigriti </p>](https://www.youtube.com/watch?v=IhPsBMBDFcg)
- [<p dir='rtl' align='right'>🔗  تصعيد الصلاحيات باستخدام ثغرة XSS sotred </p>](https://medium.com/bugbountywriteup/found-stored-cross-site-scripting-whats-next-privilege-escalation-like-a-boss-d-8fb9e606ce60)
- [<p dir='rtl' align='right'>🔗 طرق تخطي جدران الحماية لاستغلال ثغرة XSS </p>](https://medium.com/bugbountywriteup/bypassing-waf-to-perform-xss-2d2f5a4367f3)

<h4 dir='rtl' align='right'>▪️  اكتشاف ثغرات Stored XSS </h4>

- [<p dir='rtl' align='right'>🔗 تقرير عن ايجاد ثغرة stored XSS  في منصة قوقل </p>](https://blog.bentkowski.info/2018/09/another-xss-in-google-colaboratory.html)
- [<p dir='rtl' align='right'>🔗 تقرير عن مكافة احد الباحثين بمبلغ ٣١ الف دولار لاكتشاف ثغرة Stored XSS </p>](https://medium.com/@Alra3ees/google-adwords-3133-7-stored-xss-27bb083b8d27)
- [<p dir='rtl' align='right'>🔗 اكتشاف ثغرة XSS في منصة فيسبوك </p>](https://opnsec.com/2018/03/stored-xss-on-facebook/)
- [<p dir='rtl' align='right'>🔗 اكتشاف ثغرة XSS في منصة ياهو </p>](https://klikki.fi/adv/yahoo.html)
- [<p dir='rtl' align='right'>🔗 تقرير اخر  اكتشاف ثغرة XSS في منصة ياهو </p>](https://klikki.fi/adv/yahoo2.html)
- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن استغلال ثغرة Stored XSS لاستعادة الحسابات </p>](https://sites.google.com/site/bughunteruniversity/best-reports/account-recovery-xss)

<h4 dir='rtl' align='right'>▪️  اكتشاف ثغرات Stored DOM </h4>

- [<p dir='rtl' align='right'>🔗 تقرير عن ايجاد ثغرة DOM XSS </p>](https://hackerone.com/reports/297968)
- [<p dir='rtl' align='right'>🔗 ايجاد ثغرة DOM XSS في محرك البحث الخاص بالموقع المستهدف </p>](https://hackerone.com/reports/168165)
- [<p dir='rtl' align='right'>🔗 كيف تم استهداف موقع باي بال بثغرة DOM XSS </p>](https://www.rafaybaloch.com/2017/06/a-tale-of-dom-based-xss-in-paypal.html)
- [<p dir='rtl' align='right'>🔗 ايجاد ثغرة DOM XSS في موقع starbucks  </p>](https://hackerone.com/reports/526265)

<h4 dir='rtl' align='right'>▪️  اكتشاف ثغرات SSRF </h4>

- [<p dir='rtl' align='right'>🔗 جزء من موتمر DEF con  يتحدث عن SSRF </p>](https://www.youtube.com/watch?v=o-tL9ULF0KI)
- [<p dir='rtl' align='right'>🔗 كيف يتم استهداف الشبكة الداخلية من خلال استغلال ثغرة SSRF </p>](https://peertube.opencloud.lu/videos/watch/40f39bfe-6d3c-40f5-bcab-43f20944ca6a)
- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن استغلال ثغرة SSRF  والتي مكنة صائد الثغرات من رفع ملف على منصة vimeo </p>](https://medium.com/@dPhoeniixx/vimeo-upload-function-ssrf-7466d8630437)
- [<p dir='rtl' align='right'>🔗 ملخص يتحدث عن ثغرة SSRF  من الباحث nahamsec </p>](https://www.nahamsec.com/posts/my-expense-report-resulted-in-a-server-side-request-forgery-ssrf-on-lyft)

<h4 dir='rtl' align='right'>▪️  اكتشاف الثغرات </h4>

- [<p dir='rtl' align='right'>🔗 كيف يتم استخدام NMAP لاكتشاف. الثغرات </p>](https://www.peerlyst.com/posts/nmap-for-vulnerability-discovery-sachin-wagh)

<h4 dir='rtl' align='right'>▪️  ثغرات مصادقة الحسابات وتخطيها </h4>

- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن كيف يتم استغلال التوكن وسرقته.  </p>](https://medium.com/@rootxharsh_90844/abusing-feature-to-steal-your-tokens-f15f78cebf74)
- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن كيفية تخطي التحقق الثنائي في موقع Razer  </p>](https://medium.com/bugbountywriteup/how-i-was-able-to-bypass-otp-token-requirement-in-razer-the-story-of-a-critical-bug-fc63a94ad572?)
