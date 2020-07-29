<h2 dir='rtl' align='right'>الاساسيات في اختبار الاختراق  </h2>

<h3 dir='rtl' align='right'> 🧪 بيئة مختبرات اختبار الاختراق "PT" و اصطياد الثغرات "BugBounty"</h3>

## <h3 dir='rtl' align='right'>📚 جدول المحتويات  </h3>
  
### [<p dir='rtl' align='right'> 📖 تقارير المكافآت من منصات مختلفة </p>](#)
    
- [<p dir='rtl' align='right'>🔘 نصائح البداية في مجال اختبار الاختراق واصطياد الثغرات</p>](#)
- [<p dir='rtl' align='right'>🔘 🔽 اكتشاف ثغرات XSS</p>](#)
  - [<p dir='rtl' align='right'> ◀️ ثغرة XSS DOM</p>](#)
  - [<p dir='rtl' align='right'> ◀️ ثغرة XSS Stored </p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرة SSRF</p>](#)
- [<p dir='rtl' align='right'>🔘 اكتشاف الثغرات</p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات مصادقة الحسابات وتخطيها</p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات حقن الاستعلامات SQL</p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرة HTTP Desync</p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات رفع الملفات</p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات IDOR </p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات RCE </p>](#)
- [<p dir='rtl' align='right'>🔘 الطرق الصحيحة لعمليات الفحص</p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات API </p>](#)
- [<p dir='rtl' align='right'>🔘 ثغرات GraphQL </p>](#)
- [<p dir='rtl' align='right'>🔘 هاشتاقات مستخدمة في عمليات اصطياد الثغرات </p>](#)

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
- [<p dir='rtl' align='right'>🔗 كيف تم تخطي المصادقة في موقع GitHub </p>](https://blog.teddykatz.com/2019/11/05/github-oauth-bypass.html)
- [<p dir='rtl' align='right'>🔗 كيف تم سحب النطاق الفرعي بعد استغلال ثغرة في المصادقة </p>](https://hackerone.com/reports/335330)

<h4 dir='rtl' align='right'>▪️  ثغرات استغلال استعلامات SQL </h4>

- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن استغلال SQL مع الوقت باستخدام GRAPQL </p>](https://medium.com/bugbountywriteup/time-based-blind-sql-injection-in-graphql-39a25a1dfb3c)
- [<p dir='rtl' align='right'>🔗 استغلال ثغرة SQL لاستهداف موقع ستاربكس وسحب معلومات حساسة </p>](https://hackerone.com/reports/531051)
- [<p dir='rtl' align='right'>🔗 كيف تقوم بالبحث عن ثغرة SQL </p>](https://medium.com/@frycos/finding-sql-injections-fast-with-white-box-analysis-a-recent-bug-example-ca449bce6c76?)
- [<p dir='rtl' align='right'>🔗 كيف تم استهدف موقع التعدين للعملات الرقمية strynx بثغرة SQL </p>](https://strynx.org/insecure-crypto-code-execution/)
- [<p dir='rtl' align='right'>🔗 الحقن الاعمى او blind SQL في موقع mail.ru </p>](https://hackerone.com/reports/786044)
- [<p dir='rtl' align='right'>🔗 محتوى تعليمي عن اختراق المواقع المرتبة ب SQL </p>](https://blog.netspi.com/how-to-hack-database-links-in-sql-server/)


<h4 dir='rtl' align='right'>▪️ ثغرة HTTP Desync </h4>

- [<p dir='rtl' align='right'>🔗 المرجع الرسمي لاستغلال ثغرة HTTP Desync  </p>](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)
- [<p dir='rtl' align='right'>🔗 كيف تم استغلال ثغرة HTTP Desync في موقع vpn.lob.com </p>](https://hackerone.com/reports/694604)
- [<p dir='rtl' align='right'>🔗 تقرير عن استغلال ثغرة HTTP Desync لسحب حسابات المستخدمين الاخرين على منصة slack </p>](https://hackerone.com/reports/737140)

<h4 dir='rtl' align='right'>▪️ ثغرة رفع الملفات </h4>

- [<p dir='rtl' align='right'>🔗 كيف تم رفع ابواب خلفية في موقع ستاربكس </p>](https://hackerone.com/reports/506646)
- [<p dir='rtl' align='right'>🔗 كيف تم حقن خوادم فيسبوك لاستخراج بعض البيانات الحساسة </p>](https://www.vulnano.com/2019/03/facebook-messenger-server-random-memory.html)
- [<p dir='rtl' align='right'>🔗 استغلال ثغرة رفع الملفات بواسطة XML </p>](https://0xatul.github.io/posts/2020/02/external-xml-entity-via-file-upload-svg/)

<h4 dir='rtl' align='right'>▪️ ثغرة IDOR </h4>

- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن سحب الحسابات لموقع airbnb  </p>](https://www.indoappsec.in/2019/12/airbnb-steal-earning-of-airbnb-hosts-by.html)
- [<p dir='rtl' align='right'>🔗 دمج ثغرتي IDOR & graphql لاستخراج معلومات حساسة </p>](https://medium.com/@R0X4R/graphql-idor-leads-to-information-disclosure-175eb560170d)
- [<p dir='rtl' align='right'>🔗 كيف تم استغلال ثغرة IDOR وتحويلها الى RCE </p>](https://www.rahulr.in/2019/10/idor-to-rce.html?m=1)
- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن اضافة على برمجية Burp لايجاد ثغرات IDOR بشكل تلقائي </p>](https://medium.com/cyberverse/automating-burp-to-find-idors-2b3dbe9fa0b8)

<h4 dir='rtl' align='right'>▪️ ثغرة RCE </h4>

- [<p dir='rtl' align='right'>🔗 كيف يتم استغلال ثغرة RCE </p>](https://medium.com/@abhishake100/my-first-rce-stressed-employee-gets-me-2x-bounty-c4879c277e37)
- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن خطورة ثغرات RCE </p>](https://medium.com/@andrewaeva_55205/how-dangerous-is-request-splitting-a-vulnerability-in-golang-or-how-we-found-the-rce-in-portainer-7339ba24c871)

<h4 dir='rtl' align='right'>▪️ الطرق الصحيحة لعمليات الفحص </h4>

- [<p dir='rtl' align='right'>🔗 كيف يتم فحص النطاقات الفرعية من خلال شهادات SSL المتربطة بها.</p>](https://www.r00tpgp.com/2020/01/subdomain-recon-using-certificate.html?m=0)
- [<p dir='rtl' align='right'>🔗 ملاحظات تم جمعها بعد اللقاء مع الباحث nahamsec  </p>](https://mavericknerd.github.io/knowledgebase/nahamsec/recon_session_1/)
- [<p dir='rtl' align='right'>🔗 اشهر ١٠ ادوات للفحص  </p>](https://medium.com/@hackbotone/10-recon-tools-for-bug-bounty-bafa8a5961bd)
- [<p dir='rtl' align='right'>🔗 كيف تقوم بانشاء آلية لفحص النطاقات الفرعية بالشكل الصحيح </p>](https://failednuke.info/2020/recon-create-a-methodology-and-start-your-subdomain-enumeration/)
- [<p dir='rtl' align='right'>🔗   الاستخدام الصحيح عن استخدام NMAP </p>](https://securityqueens.co.uk/they-see-me-scannin-they-hatin-a-beginners-guide-to-nmap/)

<h4 dir='rtl' align='right'>▪️ ثغرات API  </h4>

- [<p dir='rtl' align='right'>🔗 مستودع نصائح خاص بثغرات API </p>](https://github.com/smodnix/31-days-of-API-Security-Tips)

<h4 dir='rtl' align='right'>▪️ ثغرات GraphQL  </h4>

- [<p dir='rtl' align='right'>🔗 تقرير يتحدث عن سحب الملاحظات واستخراجها من احد الخوادم بستخدام ثغرة GRAPHQL </p>](https://hackerone.com/reports/633001)
- [<p dir='rtl' align='right'>🔗 استغلال ثغرة GraphQl لسحب وسرقة اي عنوان  </p>](https://blog.usejournal.com/graphql-bug-to-steal-anyones-address-fc34f0374417)
- [<p dir='rtl' align='right'>🔗 كيف يتم استخدام ثغرة GraphQL لمعرفة اي بريد الالكتروني لاي مستخدم من خلال اسم المستخدم فقط </p>](https://hackerone.com/reports/792927)

<h4 dir='rtl' align='right'>▪️هاشتاقات تويتر تستحق المتابعة  </h4>

- [<p dir='rtl' align='right'>🔗 هاشتاق متخصص في اصطياد الثغرات </p>](https://twitter.com/search?q=bugbounty&src=typed_query)
- [<p dir='rtl' align='right'>🔗 هاشتاق متخصص في نصائح اصطياد الثغرات </p>](https://twitter.com/hashtag/bugbountytip?src=hashtag_click)
