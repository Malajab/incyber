<h2 dir='rtl' align='right'>الاساسيات في اختبار الاختراق  </h2><h3 dir='rtl' align='right'> 🧰 الادوات الخاصة باختبار الاختراق "PT" واصطياد الثغرات"BugBounty"</h3>

## <h3 dir='rtl' align='right'>📚 جدول المحتويات  </h3>https://www.facebook.com/profile.php?id=100005989952465&mibextid=LQQJ4d

  - [<p dir='rtl' align='right'>📢 الملقم Proxy  والتنصت على الشبكات </p>](#Proxy-&-Network-Sniffer)
  - [<p dir='rtl' align='right'>➕ الاضافات الخاصة ببرنامج Burp </p>](#Burp-Extensions) 
  - [<p dir='rtl' align='right'>🔎 فحص خوادم تطبيقات الويب   </p>](#Recon,-OSINT-&-Discovery)
  - [<p dir='rtl' align='right'>🗃 جمع المعلومات من خلال المصادر المفتوحة </p>](#Exploitation)
  - [<p dir='rtl' align='right'>🔎 ادوات الفحص</p>](#Scanners)
  - [<p dir='rtl' align='right'>📱 اختراق الهواتف الذكية </p>](#Mobile-Hacking)
  - [<p dir='rtl' align='right'>🧾 قائمة البرامج الخاصة بنظام كالي لينكس </p>](#Kali-tools)
  - [<p dir='rtl' align='right'>📚 مصادر مفيدة لاختبار الاختراق  </p>](#resource)
  - [<p dir='rtl' align='right'>📝 برامج جمع المذكرات والملاحظات  </p>](#Exploitation)
  - [<p dir='rtl' align='right'>🪓 ادوات الاختراق  </p>](#Exploitation)

  
  ## <h3 dir='rtl' align='right'>📢 خادم الوكيل Proxy  والتنصت على الشبكات </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> اللغة المستخدمة </th>
    <th> الموقع </th>
    <tr>
    <td> اداة Burp Suite </td> 
    <td>تقوم الاداة بعتراض الاتصال والتعديل عليه قبل ارساله الى الخادم</td>
    <td>لغة الجافا </td>
    <td>https://portswigger.net/burp</td>
  </tr>  
      <tr>
    <td> اداة OWASP Zap Proxy </td> 
    <td>تقوم الاداة بعتراض الاتصال والتعديل عليه قبل ارساله الى الخادم</td>
    <td>لغة الجافا </td>
    <td>www.owasp.org</td>
  </tr> 
      <tr>
    <td> اداة netsniff-ng </td> 
    <td> تقوم الاداة بعتراض الاتصال وقراءة البيانات بشكل مفصل </td>
    <td>لغة C, C++ </td>
    <td>https://github.com/netsniff-ng/netsniff-ng</td>
  </tr> 
        <tr>
      <tr>
    <td> اداة tcpdump/libpcap </td> 
    <td> تقوم الاداة بعتراض الاتصال وقراءة البيانات بشكل مفصل </td>
    <td>لغة C, C++ </td>
    <td>http://www.tcpdump.org/</td>
  </tr> 
        <tr>
    <td> اداة Wireshark </td> 
    <td> تقوم الاداة بعتراض الاتصال وقراءة البيانات بشكل مفصل </td>
    <td>لغة C, C++ </td>
    <td>www.wireshark.org</td>
  </tr> 
  </tr>
  </table>
  
 ## <h3 dir='rtl' align='right'>➕ اضافات برنامج Burp </h3>
 <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> اللغة المستخدمة </th>
    <th> الموقع </th>
    <tr>
    <td> اضافة Logger++ </td>
    <td>تقوم الاداة بحفظ جميع الاتصالات التي يقوم بها البرنامج واستخراجها على شكل CSV</td>
    <td>لغة الجافا </td>
    <td>https://portswigger.net/</td>
  </tr>
      <tr>
    <td> اضافة Flow </td>
    <td>تقوم هذه الاضافة بحفظ جميع الطلبات التي يقوم بها البرنامج وتصفيتها حسب الطلب</td>
    <td>لغة الجافا </td>
    <td>https://portswigger.net/</td>
  </tr>
      <tr>
    <td> اضافة AuthMatrix  </td>
    <td>تقوم هذه الاداة باختبار تصاريح الوصول وايجاد الثغرات بها وعرضها على شكل جدول لكي تتضح الصورة بشكل كامل </td>
    <td>لغة python </td>
    <td>https://portswigger.net</td>
  </tr> 
  <tr>
  <td> اضافة Autorize  </td>
  <td>تقوم هذه الاداة بمساعدة مختبر الاختراق لرصد واكتشاف نقاط الضعف في عمليات تصريح الدخول </td>
  <td>لغة python </td>
  <td>https://portswigger.net</td>
  </tr> 
  <td> اضافة Auto Repeater  </td>
  <td>الهدف من هذه الاداة هو ارسال الطلبات بشكل تلقائي مع تغير بعض المعايير التي يحددها مختبر الاختراق </td>
  <td>لغة الجافا </td>
  <td>https://portswigger.net</td>
   </tr>
  <td> اضافةProgress Tracker  </td>
  <td>تقوم هذه الاضافة بتتبع حالة اختبار الاختراق او اصطياد التهديدات ومستوى التقدم بها </td>
  <td>لغة الجافا </td>
  <td>https://portswigger.net</td>
    </tr>
      <td> اضافة HUNT  </td>
  <td>تقوم هذه الاداة بفحص بفحص الثغرات واستخراجها وهي مخصصة لثغرات SQL وثغرة IDOR </td>
  <td>لغة الجافا </td>
  <td>https://portswigger.net</td>
  </tr>
  <td> اضافة Mind Map Exporter  </td>
  <td>  وظيفة هذه الاداة رسم الخارطة الذهنية لجيمع الروابط الخاصة بالموقع الذي يتم فحصة </td>
  <td>لغة الجافا </td>
  <td>https://portswigger.net</td>
  </tr>
  <td> اضافة Burp JS link finder  </td>
  <td> تقوم الاداة باستخراج جميع الروابط من ملفات JS والتي قد يكون بعضها يحتوى على معلومات حساسة </td>
  <td>لغة الجافا </td>
  <td>https://portswigger.net</td>
   </tr>
   <td> اضافة BurpParser  </td>
  <td> استخراج جميع الروابط الخاصة بالهدف وجمعها في ملف XML لتسهيل عمل التحليل اليدوي </td>
  <td>لغة python </td>
  <td>https://github.com/billdeitrick/burpparser</td>
   </tr>
   <td> اضافة BurpSuite_payloads  </td>
  <td> مجموعة من الادوات التي تفيدك في عملية استخدام "Intruder" </td>
  <td>لا يوجد </td>
  <td>https://github.com/thegsoinfosec/BurpSuite_payloads</td>
   </tr>
  </table>

  ## <h3 dir='rtl' align='right'>🔎 فحص خوادم تطبيقات الويب </h3>
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> اللغة المستخدمة </th>
    <th> الموقع </th>
    <tr>
    <td> اداة FFuF </td>
    <td>من الادوات التي استخدمها بشكل يومي وهي تقوم بمحاولة تخمين الامتدادات الخاصةبالمواقع وكما يميز هذه الاداة هي امكانية تخصييها حسب رغبتك</td>
    <td> لغة Go </td>
    <td>https://github.com/ffuf/ffuf</td>
  </tr>
      <tr>
    <td> اداة Sublist3r </td>
    <td>تقوم هذه الاداة بحصر وجمع جميع النطاقات الفرعية الخاصة بالموقع المستهدف مستعينة بالخدمات العامة مثل قوقل ياهو وغيرها </td>
    <td> لغة python </td>
    <td>https://github.com/aboul3la/Sublist3r/</td>
  </tr>
      <tr>
    <td>  اداة   dirsearch  </td>
    <td> تقوم هذه  الاداة بمحاولة تخمين الامتدادات الخاصة بالموقع المستهدف وهي اداة سهلة الاستخدام وكذلك قوية الاداء </td>
    <td>لغة python </td>
    <td>https://github.com/maurosoria/dirsearch</td>
  </tr>
  <tr>
  <td> اضافة Autorize  </td>
  <td>تقوم هذه الاداة بمساعدة مختبر الاختراق لرصد واكتشاف نقاط الضعف في عمليات تصريح الدخول </td>
  <td>لغة python </td>
  <td>https://portswigger.net</td>
  </tr>
  <td> اداة Amass  </td>
  <td>تقوم هذه الاداة باستخدام تقنيات مختلفة لحصر النطاقات الفرعية للموقع المستهدف  </td>
  <td>لغة الجافا </td>
  <td>https://github.com/OWASP/Amass</td>
    </tr>
  <td> اضافة BuiltWith  </td>
  <td>اضافة على المتصفح حيث تستطيع هذة الاداة التعرف على اكثر من ٨١ الف تطبيق وبرمجية والهدف منها هو اعطائك معلومات اكثر  عن المنصة المستخدمة في الموقع المستهدف  </td>
  <td> لغة JavaScript </td>
  <td>https://builtwith.com</td>
    </tr>
    <td>  اداة findomain  </td>
    <td> اداة تستخدم  منصات متعددة لايجاد النطاقات الفرعية </td>
    <td>Rust </td>
    <td>https://github.com/Edu4rdSHL</td>
  </tr>
  <td> اداة waybackurls  </td>
  <td>تقوم باستخرج جميع الصفحات المؤرشفة للموقع المستهدف </td>
  <td> لغة Go </td>
  <td>https://github.com/tomnomnom</td>
  </tr>
  <td> اداة  Meg  </td>
  <td> تقوم الاداة بمحاولة تخمين جميع المسارات المتاحة على الموقع المستهدف حيق تعمل الاداة بشكل مختلف حيث تقوم الاداة بفحص المسار الواحد بشكل كامل قبل الانتقال الى المسار التالي </td>
  <td> لغة Go </td>
  <td>https://github.com/tomnomnom/meg</td>
  </tr>
  <td> اداة  Osmedeus  </td>
  <td> منصة تقوم بالفحص بشكل تلقائي وهي  مفيدة لعمليات اختبار وتقييم الاختراقات  </td>
  <td> لغة Python </td>
  <td>https://github.com/j3ssie/Osmedeus</td>
  </tr>
  <td> اداة  Reconness  </td>
  <td> اداة تقوم بجميع جميع عمليات الفحص وترتيبها في مكان واحد  </td>
  <td> لغة C++ </td>
  <td>https://github.com/reconness</td>
  </tr>
  <td> اداة  knock  </td>
  <td>تقوم بعمليات جمع للنطاقات الفرعية للموقع المستهدف  </td>
  <td> لغة Go </td>
  <td>https://github.com/guelfoweb/knock</td>
  </tr>
  <td> اداة  SpiderFoot  </td>
  <td>هي منصة تقوم باستخدام اكثر من ١٠٠ مصدر لجمع المعلومات عن الموقع المستهدف   </td>
  <td> لغة Python </td>
  <td>https://github.com/smicallef/spiderfoot</td>
    </tr>
  <td> اداة  DNSDumpster  </td>
  <td> اداة متميزة في حصر وجمع النطاقات الفرعية للموقع المستهدف </td>
  <td> لغة JavaScript  </td>
  <td>https://dnsdumpster.com/</td>
      </tr>
  <td> اداة  masscan  </td>
  <td> اداة تقوم بعمليات فحص للعناوين IP والمنفاذ بشكل سريع جداً </td>
  <td> لغة C  </td>
  <td>https://github.com/robertdavidgraham/masscan</td>
        </tr>
  <td> اداة  dnsenum   </td>
  <td> اداة تقوم بحصر وجمع المعلومات عن النطاقات الفرعية للموقع المستهدف </td>
  <td> لغة Perl  </td>
  <td>https://github.com/fwaeytens/dnsenum/</td>
      </tr>
  <td> اداة  dnsmap </td>
  <td>  اداة تقوم بحصر وجمع المعلومات عن النطاقات الفرعية للموقع المستهدف من غير التواصل معه بشكل مباشر </td>
  <td> لغة C </td>
  <td>https://github.com/makefu/dnsmap/</td>
        </tr>
  <td> اداة  SSLyze </td>
  <td> تساعد هذه الاداة على تحليل شهادات SSL لمعرفة مكامن نقاط الضعف والاعدادات الخاطئة </td>
  <td> لغة pthton </td>
  <td>https://github.com/nabla-c0d3/sslyze</td>
          </tr>
  <td> اداة  Nikto </td>
  <td> اداة سريعة جداً في استخراج نقاط الضعف والثغرات ولكن سهلة الاكتشاف من الخوادم المستهدفة بسبب كمية البيانات المشبوهة التي ترسلها الاداة </td>
  <td> لغة pthton </td>
  <td>https://cirt.net/nikto2</td>
            </tr>
  <td> اداة  WPScan  </td>
  <td>الاداة تقوم بعمل اختبار اختراق وايجاد الثغرات وكسر كلمات المرور. وهي متخصصة في استهدافة منصات Wordpress </td>
  <td> لغة pthton </td>
  <td>https://wpscan.org/</td>
            </tr>
  <td> اداة  joomscan </td>
  <td>الاداة تقوم بعمل اختبار اختراق وايجاد الثغرات وكسر كلمات المرور. وهي متخصصة في استهدافة منصات Joomla </td>
  <td> لغة pthton </td>
  <td>https://www.owasp.org/index.php/Category</td>
            </tr>
  <td> اداة  XSpear </td>
  <td>تقوم هذه الأداة بإيجاد ثغرات XSS وتصنيف خطورتها وتمكنك من طباعة تقرير مفصل بمستوى خطورة الثغرة</td>
  <td> لغة Ruby </td>
  <td>https://github.com/hahwul/XSpear</td>
  
  </table>


 ## <h3 dir='rtl' align='right'>🗃 جمع المعلومات من خلال المصادر المفتوحة </h3>
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> الموقع </th>
    <tr>
    <td> اداة hunter </td>
    <td>تقوم الاداة بجمع المعلومات عن البريد الالكتروني للموقع المستهدف</td>
    <td>https://hunter.io</td>
    <tr>
    <td> اداة intelx </td>
    <td>تقوم الاداة بجمع المعلومات بشكل متكامل عن للموقع المستهدف</td>
    <td>https://intelx.io</td>
          <tr>
    <td> اداة Shodan </td>
    <td>تقوم الاداة بجمع المعلومات عن الاجهزة المتصلة بالانترنت وكذلك تقوم الاداة بجمع بعض المعلومات الاستخباراتية واجراء بعض الفحوصات للبحث عن الثغرات</td>
    <td>https://www.shodan.io/</td>
      <tr>
    <td> اداة Lookyloo </td>
    <td>تقوم بالتواصل مع الموقع المستهدف وجمع المعلومات عنه من خلال زيارة الروابط الخاصة به واستخراجها بخاطة ذهنية</td>
    <td>https://lookyloo.circl.lu/scrape</td>
         <tr>
    <td> اداة Censys </td>
    <td>تقوم الاداة بجمع المعلومات بشكل متكامل عن للموقع المستهدف وخصوصا فيما يتعلق بالعناوين IPs ويعطي معلومات شبة مفصلة</td>
    <td>https://censys.io/</td>
           <tr>
    <td> اداة crt.sh </td>
    <td>اداة مخصصة للبحث عن المواقع المرتبطة باحد الشهادات للموقع المستهدف</td>
    <td>https://censys.io/</td>
            <tr>
    <td> اداة Virus Total </td>
    <td>على عكس محللي البرمجيات الخبيثة يتم استخدام Virus Total للبحث عن النطاقات الفرعية للموقع المستهدف وكذلك معرفة عنوان IP</td>
    <td>https://www.virustotal.com/</td>
            <tr>
    <td> اداة Spyse </td>
    <td>محرك بحث جديد وهو موجة للمتخصين في اختبار الاختراق وصائدي الثغرات</td>
    <td>https://Spyse.com</td>
             <tr>
    <td> اداة ZoomEye </td>
    <td> محرك بحث صيني جديد للبحث عن الانظمة المتصلة بالانترنت </td>
    <td>https://www.zoomeye.org/</td> 
              <tr>
    <td> اداة NerdyData </td>
    <td>محرك بحث جديد متخصص للبحث عن الاكواد المصدرية</td>
    <td>https://nerdydata.com/</td>
             <tr>
    <td> اداة DataSploit  </td>
    <td>اداة تقوم بعرض مخرجات محركات البحث الاخرى بشكل تحليلي</td>
    <td>https://github.com/upgoingstar/datasploit</td>
             <tr>
    <td> اداة Sn1per </td>
    <td>منصة متكاملة لجمع المعلومات لمختبري الاختراق</td>
    <td>https://github.com/1N3/Sn1per</td>
               </tr>
       </table>   
       
  ## <h3 dir='rtl' align='right'>🔎 ادوات فحص الشبكات </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> الموقع </th>
    <tr>
    <td> اداة NMAP </td>
    <td>اداة تقوم بالبحث عن المنافذ المفتوحة على الشبكة المستهدفة</td>
    <td>https://nmap.org</td>
    </tr> 
      <tr>
    <td>  مستودع KeyHacks  </td>
    <td>تقوم بحصر وجمع جميع API التي تم كتابة تقارير سابقه عنها في منصات مكآفات الثغرات</td>
    <td>https://github.com/streaak/keyhacks</td>
               </tr>
       </table>   

  ## <h3 dir='rtl' align='right'>📱 ادوات اختبار اختراق الهواتف الذكية </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> الموقع </th>
    <tr>
    <td> اداة jadx </td>
    <td>تقوم بقراءة الكود المصدري للتطبيق</td>
    <td>https://github.com/skylot/jadx</td>
       </tr>
      <tr>
    <td> اداة dex2jar </td>
    <td>تقوم بقراءة الكود المصدري للتطبيق</td>
    <td>https://github.com/pxb1988/dex2jar</td>
       </tr>
        <tr>
    <td> منصة Mobile Security Framework (MobSF)  </td>
    <td>تقوم المنصة بتحليل التطبيق بشكل كامل من نواحي متعددة سواء كانت ثغرات او برمجيات خبيثة</td>
    <td>https://github.com/MobSF/Mobile-Security-Framework-MobSF/</td>
       </tr>
       </table>  
       
   ## <h3 dir='rtl' align='right'>🧾 قائمة البرامج الخاصة بنظام كالي لينكس </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <tr>
    <td>جمع المعلومات Information Gathering‬‬‬ </td>
    <td>تشمل على قائمة أدوات استطلاع تستخدم لجمع البيانات من الشبكات والأجهزة المستهدفة.</td>
       </tr>
      <tr>
    <td> أدوات الاستغلال ‪Exploitation Tools‬‬ </td>
    <td>‫في هذه القائمة تجد الأدوات التي تُستخدم في استغلال الثغرات التي قمت باكتشافها في نظام ما. كما يمكنك عمل صفحات مزورة واستهداف الراوترات.
</td>
       </tr>
        <tr>
    <td> تحليل الثغرات Vulnerability Analysis‬‬</td>
    <td>‬تجد هنا الأدوات التي تساعدك على اكتشاف الثغرات في الأنظمة المستهدفة كما يمكنك استخدامها للقيام بعملية جمع المعلومات.</td>
       </tr>
        <tr>
    <td> الهجمات على الشبكات اللاسلكية Wireless Attack </td>
    <td>‬تتضمن الأدوات المستخدمة لاستغلال الثغرات في بروتوكولات الشبكات اللاسلكية و البلوتوث وثغرات تحديد الهوية باستخدام موجات الراديو RFID - (Radio-frequency Identification ) والتقنية عباره عن تحديد الهوية بشكل تلقائي بالاعتماد على جهاز يسمى (RFID Tags).</td>
       </tr>
          <tr>
    <td>  التحليل الجنائي ‪Forensics‬‬ </td>
    <td>تضم القائمة الأدوات التي تساعدك في مراقبة وتحليل بيانات وتطبيقات الشبكات. تشمل استرداد وبحث المواد الموجودة على الأجهزة الرقمية والتي ترتبط كثيرا بالجرائم الرقمية.</td>
       </tr>
            <tr>
    <td>  تحليل تطبيقات الويب Web Applications Analysis </td>
    <td>في الجزء تستطيع فحص واستغلال الثغرات في سيرفرات الويب.</td>
       </tr>
            <tr>
    <td>  اختبار مدى قدرة الخوادم على تحمل هجمات حجب الخدمة Stress Testing </td>
    <td>مؤكد أن سمعت بهجمات DDoS وهي هجمات الحرمان من الخدمات أو هجوم حجب الخدمة ‏تتم عن طريق إغراق المواقع بسيل من البيانات غير اللازمة يتم إرسالها عن طريق أجهزة مصابة.في هذه القائمة تجد الأدوات التي تساعدك لمعرفة مدى تحمل البرامج والسيرفرات للمستخدمين.</td>
       </tr>
            <tr>
    <td>التنصت وانتحال الشخصية Sniffing and Spoofing‬‬</td>
    <td>‫‬يتضمن هذا الجزء الأدوات التي تقوم بإلتقاط حِزم البيانات في الشبكات. من هنا تستطيع انتحصال الشخصية من خلال تعديل حزم البيانات.</td>
       </tr>
            <tr>
    <td>   أدوات تثبيت الاختراق Maintaining Access </td>
    <td>‬‬ بعد قيامك بعملية الاختراق سوف تحتاج لأدوات تستعملها لتثبيت الاختراق لضمان الوصول للأنظمة.
من خلال هذه الأدوات ستتمكن من ذلك.</td>
       </tr>
              <tr>
    <td> الهجمات كسر كلمة المرور Password Attacks </td>
    <td>تشتمل الادوات التي تقوم بهجمات كسر كلمات المرور‬‬ ‫وهجمات تخمين كلمة السر </td>
       </tr>
              <tr>
    <td> أدوات إعداد التقارير Reporting Tools </td>
    <td>‬‬حين اكتمال ماتوصلت إليه من معلومات ستقوم بإعداد تقرير شامل يحتوي على الأدوات المستخدمة وهنا سوف تجدها.</td>
       </tr>
              <tr>
    <td> الهندسة العكسية Reverse Engineering‬‬ </td>
    <td>‬‬ ‫‬في الهندسة العكسية هنالك العديد من الأدوات التي تساعدك في قراءة.البرمجيات الخبيثة واستخراج التعليمات البرمجية الضارة او مؤشرات الاختراق </td>
       </tr>
       </table>  
       
  ## <h3 dir='rtl' align='right'>📚 مصادر متعددة </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>المصدر </th>
    <th> الوصف </th>
    <th> الموقع </th>
    <tr>
    <td> مصدر SecLists </td>
    <td>مصدر يحتوى على قوائم متعددة تستخدم في اختبار الاختراق واصطياد الثغرات وانصح باستخدامها </td>
    <td>https://github.com/danielmiessler/SecLists</td>
       </tr>
      <tr>
    <td> اداة CyberChef </td>
    <td>اداة غنية عن التعريف تقوم بفك وتشفير </td>
    <td>https://gchq.github.io/CyberChef/</td>
       </tr>
        <tr>
    <td> مصدر PayloadsAllTheThings  </td>
    <td>يحتوي على جميع ما تحتاجة عند قيامك بختبار الاختراق لتطبيقات الويب</td>
    <td>https://github.com/swisskyrepo/PayloadsAllTheThings</td>
       </tr>
       </table>  
       
   ## <h3 dir='rtl' align='right'>📝 برامج جمع المذكرات والملاحظات </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>المصدر </th>
    <th> الوصف </th>
    <th> الموقع </th>
    <tr>
    <td> برمجية  Reconness </td>
    <td>تقوم بجمع وتنظيم المخرجات من عملية اختبار الاختراق من ملاحظات ومخرجات الادوات  </td>
    <td>https://github.com/reconness/reconness</td>
       </tr>
      <tr>
    <td> برمجية notion </td>
    <td>اداة استخدمها شخصياً جميلة جداً في جمع الملاحظات وتستطيع تحميلها على اجهزة مختلفة حيث تقوم بالربط بينهم من خلال بريدك الالكتروني </td>
    <td>https://www.notion.so</td>
       </tr>
        <tr>
    <td> برمجية xmind  </td>
    <td>تقوم البرمجية برسم خارطة ذهنية للموقع المستهدف </td>
    <td>https://www.xmind.net/</td>
       </tr>
       </table>        
       
 
       
  ## <h3 dir='rtl' align='right'>🪓 ادوات الاختراق </h3>
  
  <table dir='rtl' align="right">
  <tr>
    <th>اسم الاداة </th>
    <th> الوصف </th>
    <th> الموقع </th>
    <tr>
    <td> اداة SQLMAP </td>
    <td>اداة مفتوحة المصدر تقوم بختبار واتمتة عمليات اختبار واستغلال ثغرة SQL</td>
    <td>http://sqlmap.org</td>
       </tr>
       </table>        
 
