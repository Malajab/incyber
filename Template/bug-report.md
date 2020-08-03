<h2 dir='rtl' align='right'>📝 تقرير اصطياد الثغرات BugBounty Report </h2>

## <h3 dir='rtl' align='right'>📖 مقدمة </h3>

>  <p dir='rtl' align='right'> سنقوم هنا بذكر اكثر نماذج التقارير المستخدمة في اصطياد الثغرات BugBounty ورفعها الى المنصات بشكل واضح.
</p>

>  <p dir='rtl' align='right'> ان احد اهم العناصر في منصات مكافاة الثغرات هي التقارير التي يتم رفعها ومدى جودته٫الذي قد يؤثر على مستوى التقييم من قبل الفريق المختص وقد يساهم في معظم المنصات في زيادة المكافات لذلك احرص على جودة التقرير ولا تدع العجلة في رفع التقرير تسبب لك عدم قبول تقريرك
</p>


<h5 dir='rtl' align='right'>▪️ ادوات مساعدة لكتابة التقارير </h5>

- [<p dir='rtl' align='right'>🔗  موقع stackedit لتنسيق التقرير اونلاين </p>](https://stackedit.io/)
- [<p dir='rtl' align='right'>🔗  برنامج haroopress لانظمة ويندوز  </p>](http://pad.haroopress.com/)
- [<p dir='rtl' align='right'>🔗  برنامج macdown لانظمة ماك  </p>](http://macdown.uranusjr.com/)
- [<p dir='rtl' align='right'>🔗  برنامج remarkableapp لانظمة لينكس  </p>](https://remarkableapp.github.io/)

## <h4 dir='rtl' align='right'>📚 محتويات التقرير  </h4>

## <h5 dir='rtl' align='right'> العنوان - Title  </h5>

>  <p dir='rtl' align='right'> عنوان التقرير هو سطر واحد يتم عنونة التقرير به ويجب ان يكون مختصر وواضح بحيث يتم ذكر نوع الثغرة و التأثير المتوقع و ماهو النطاق المصاب 
</p>

<h5 dir='rtl' align='right'>▪️ مثال علي العنوان - Title </h5>

>  <p dir='rtl' align='right'>IDOR in profile lead to account takeover on github.com 
</p>

## <h5 dir='rtl' align='right'> الوصف - Description </h5>

>  <p dir='rtl' align='right'> يتم شرح الثغرة بالمختصر المفيد ويتم ذكر تفاصيل الثغرة ومكانها وسبب حدوثها والاوامر الاضاف في حال وجودها لكي يتم تطبيق الثغرة لذلك كما ذكرت في بداية الوصف شرح مفصل ومختصر 
</p>

<h5 dir='rtl' align='right'>▪️ مثال على الوصف - Description </h5>

>  <p dir='rtl' align='right'>Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted web sites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user.
</p>

## <h5 dir='rtl' align='right'> خطوات استغلال الثغرة -  Steps to reproduce  </h5>

>  <p dir='rtl' align='right'> ان الهدف الاساسي من هذةالخطوة هو شرح كيف يتم استغلال الثغرة بالتفصيل والخطوات والترتيب الصحيح لكي يتم استغلالها وهو اهم جزء في التقرير 
</p>

<h5 dir='rtl' align='right'>▪️ مثال على خطوات استغلال الثغرة -  Steps to reproduce </h5>

>  <p dir='rtl' align='right'>1- visit this link 2- click on the profile tab 
</p>

>  <p dir='rtl' align='right'> اذا كنت تستخدم Burp لاستغلال الثغرة يفضل ذكر محتوى الاتصال بشكل كامل كما في الاسفل 
</p>


```
GET /test.php?page=/etc/issue HTTP/1.1
Host: test.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Cookie: _ga=GA1.2.1344627302.1544974513; _gid=GA1.2.395150311.1544974513; PHPSESSID=cfpt3iskot4sfbjhjvf192je2f; security_level=0
Connection: close
```

## <h5 dir='rtl' align='right'> خطورة الثغرة Impact  </h5>

>  <p dir='rtl' align='right'> يتم شرح الخطورة التي تنتج عن الثغرة مع العلم ان الخطورة تتغير بتغير الموقع المستهدف وحساسية البيانات ومدى الاستغلال 
</p>

<h5 dir='rtl' align='right'>▪️ مثال على الخطورة - Impact </h5>

>  <p dir='rtl' align='right'> This issue will affect all users on the site who view the profile of the attacker, when the image is rendered the payload is executed instead of a profile image. Additionally when the malicious user posts anything on the forums the payload will execute. 
</p>

## <h5 dir='rtl' align='right'> التوصيات لاصلاح الثغرة - Recommendation </h5>

>  <p dir='rtl' align='right'> يتم هنا شرح وسرد جميع الخطوات والتوصيات الضرورية لاغلاق الثغرة ويفضل الاستعانة بافضل الامتثالات مثل موقع OWASP وغيره. 
</p>

<h5 dir='rtl' align='right'>▪️ مثال على التوصيات - Recommendation </h5>

>  <p dir='rtl' align='right'> Insure that file upload checks the MIME type of content being uploaded, for additional security implement server side content checking to ensure file headers match that of the file extension. Additionally make sure that all user input is treated as dangerous do not render any HTML tags.
</p>

## <h5 dir='rtl' align='right'> نماذج جاهزة لكتابة التقارير </h5>

- [<p dir='rtl' align='right'>🔗  نموذج متكامل  </p>](https://github.com/ZephrFish/BugBountyTemplates/blob/master/Blank.md)
- [<p dir='rtl' align='right'>🔗  نموذج موقع hackerone   </p>](https://docs.hackerone.com/hackers/quality-reports.html)
