<div dir="rtl" align='right'>

## Persistence الاصرار 


### لتحميل بصيغ متعددة تفضل:
- صيغة JSON :[تفضل هنا]() 
- صيغة XLS :[تفضل هنا]()
- صيغة CSV :[تفضل هنا]() 
- صيغة XML :[تفضل هنا]()
- صيغة SQL :[تفضل هنا]()
- صيغة YML :[تفضل هنا]()
 
### التقنيات / Techniques

| ID / المعرف | المعرف الفرعي | الاسم/ Name                                                                            |  الوصف / Description |
|-------------|---------------|----------------------------------------------------------------------------------------|----------------------|
| T1098       |               | التلاعب بالحسابات / Account Manipulation                                               |                      |
| T1098       | .001          | بيانات الاعتماد السحابية / Additional Cloud Credentials                                |                      |
| T1098       | .002          | تفويض الصلاحيات على مستوى البريد / Exchange Email Delegate Permissions                 |                      |
| T1098       | .003          | اضافة صلاحيات مدير النظام لخدمات 356 اوفيس / Add Office 365 Global Administrator Role  |                      |
| T1098       | .004          | مفاتيح التصاريح لخدمات SSH/ SSH Authorized Keys                                        |                      |
| T1197       |               | BITS Jobs                                                                              |                      |
| T1547       |               | تسجيل الدخول التلقائي / Boot or Logon Autostart Execution                              |                      |
| T1547       | .001          | مفاتيح التسجيل والتشغيل التلقائي/ Registry Run Keys / Startup Folder                   |                      |
| T1547       | .002          | تصاريح الحزم / Authentication Package                                                  |                      |
| T1547       | .003          | Time Providers                                                                         |                      |
| T1547       | .004          | Winlogon Helper DLL                                                                    |                      |
| T1547       | .005          | Security Support Provider                                                              |                      |
| T1547       | .006          | Kernel Modules and Extensions                                                          |                      |
| T1547       | .007          | Re-opened Applications                                                                 |                      |
| T1547       | .008          | LSASS Driver                                                                           |                      |
| T1547       | .009          | Shortcut Modification                                                                  |                      |
| T1547       | .010          | مراقبة المنافذ / Port Monitors                                                         |                      |
| T1547       | .011          | Plist Modification                                                                     |                      |
| T1547       | .012          | طباعة  العمليات / Print Processors                                                     |                      |
| T1037       |               | الاقلاع او الدخول التلقائي / Boot or Logon Initialization Scripts                      |                      |
| T1037       | .001          | سكربت الدخول بيئة ويندوز / Logon Script (Windows)                                      |                      |
| T1037       | .002          | سكربت الدخول بيئة ماك / Logon Script (Mac)                                             |                      |
| T1037       | .003          | سكربت الدخول لشبكات / Network Logon Script                                             |                      |
| T1037       | .004          | Rc.common                                                                              |                      |
| T1037       | .005          | ادوات بدء التشغيل / Startup Items                                                      |                      |
| T1176       |               | اضافات المتصفح / Browser Extensions                                                    |                      |
| T1554       |               | اختراق برمجيات المستخدم / Compromise Client Software Binary                            |                      |
| T1136       |               | انشاء حساب / Create Account                                                            |                      |
| T1136       | .001          | حساب محلي / Local Account                                                              |                      |
| T1136       | .002          | حساب مدير نظام / Domain Account                                                        |                      |
| T1136       | .003          | حساب على الخدمات السحابية / Cloud Account                                              |                      |
| T1543       |               | انشاء او تعديل العمليات على الانظمة / Create or Modify System Process                  |                      |
| T1543       | .001          | تفعيل البرمجية / Launch Agent                                                          |                      |
| T1543       | .002          | خدمات النظام / Systemd Service                                                         |                      |
| T1543       | .003          | خدمات الويندوز / Windows Service                                                       |                      |
| T1543       | .004          | Launch Daemon                                                                          |                      |
| T1546       |               | تنفيذ الاحداث حسب المعطيات /  Event Triggered Execution                                |                      |
| T1546       | .001          | تعديل الملف الافتراضي / Change Default File Association                                |                      |
| T1546       | .002          | شاشة التوقف/ Screensaver                                                               |                      |
| T1546       | .003          | Windows Management Instrumentation Event Subscription                                  |                      |
| T1546       | .004          | .bash_profile and .bashrc                                                              |                      |
| T1546       | .005          | Trap                                                                                   |                      |
| T1546       | .006          | LC_LOAD_DYLIB Addition                                                                 |                      |
| T1546       | .007          | Netsh Helper DLL                                                                       |                      |
| T1546       | .008          | Accessibility Features                                                                 |                      |
| T1546       | .009          | AppCert DLLs                                                                           |                      |
| T1546       | .010          | AppInit DLLs                                                                           |                      |
| T1546       | .011          | Application Shimming                                                                   |                      |
| T1546       | .012          | Image File Execution Options Injection                                                 |                      |
| T1546       | .013          | PowerShell Profile                                                                     |                      |
| T1546       | .014          | Emond                                                                                  |                      |
| T1546       | .015          | Component Object Model Hijacking                                                       |                      |
| T1133       |               | خدامات الاتصال عن بعد External Remote Services                                         |                      |
| T1574       |               | انتحال مجال التنفيذ / Hijack Execution Flow                                            |                      |
| T1574       | .001          | DLL Search Order Hijacking                                                             |                      |
| T1574       | .002          | DLL Side-Loading                                                                       |                      |
| T1574       | .004          | Dylib Hijacking                                                                        |                      |
| T1574       | .005          | Executable Installer File Permissions Weakness                                         |                      |
| T1574       | .006          | LD_PRELOAD                                                                             |                      |
| T1574       | .007          | Path Interception by PATH Environment Variable                                         |                      |
| T1574       | .008          | Path Interception by Search Order Hijacking                                            |                      |
| T1574       | .009          | Path Interception by Unquoted Path                                                     |                      |
| T1574       | .010          | Services File Permissions Weakness                                                     |                      |
| T1574       | .011          | Services Registry Permissions Weakness                                                 |                      |
| T1574       | .012          | COR_PROFILER                                                                           |                      |
| T1525       |               | تفعيل نسخة صورية / Implant Container Image                                             |                      |
| T1137       |               | خدمات الاوفيس مع بدء التشغيل / Office Application Startup                              |                      |
| T1137       | .001          | ملفات المايكرو / Office Template Macros                                                |                      |
| T1137       | .002          | Office Test                                                                            |                      |
| T1137       | .003          | Outlook Forms                                                                          |                      |
| T1137       | .004          | الصفحة الرئيسية لبرنامج استخدام البريد / Outlook Home Page                             |                      |
| T1137       | .005          | القواعد في رنامج استخدام البريد / Outlook Rules                                        |                      |
| T1137       | .006          | الاضافات Add-ins                                                                       |                      |
| T1542       |               | نظام اقلاع جاهز / Pre-OS Boot                                                          |                      |
| T1542       | .001          | System Firmware                                                                        |                      |
| T1542       | .002          | Component Firmware                                                                     |                      |
| T1542       | .003          | برمجية ضارة مع اقلاع النظام / Bootkit                                                  |                      |
| T1542       | .004          | ROMMONkit                                                                              |                      |
| T1542       | .005          | TFTP Boot                                                                              |                      |
| T1053       |               | Scheduled Task/Job                                                                     |                      |
| T1053       | .001          | بيئة لينكس / At (Linux)                                                                |                      |
| T1053       | .002          | بيئة ويندوز / At (Windows)                                                             |                      |
| T1053       | .003          | Cron                                                                                   |                      |
| T1053       | .004          | Launchd                                                                                |                      |
| T1053       | .005          | جدولة المهام Scheduled Task                                                            |                      |
| T1053       | .006          | Systemd Timers                                                                         |                      |
| T1505       |               | Server Software Component                                                              |                      |
| T1505       | .001          | SQL Stored Procedures                                                                  |                      |
| T1505       | .002          | Transport Agent                                                                        |                      |
| T1505       | .003          | ابواب خلفية Web Shell                                                                  |                      |
| T1205       |               | Traffic Signaling                                                                      |                      |
| T1205       | .001          | Port Knocking                                                                          |                      |
| T1078       |               | حساب فعال / Valid Accounts                                                             |                      |
| T1078       | .001          | حساب افتراضي / Default Accounts                                                        |                      |
| T1078       | .002          | حساب مدير النظام / Domain Accounts                                                     |                      |
| T1078       | .003          | حساب محلي / Local Accounts                                                             |                      |
| T1078       | .004          | حساب الخدمات السحابية / Cloud Accounts                                                 |                      |


</div>
