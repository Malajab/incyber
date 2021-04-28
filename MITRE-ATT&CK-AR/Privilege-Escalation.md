<div dir="rtl" align='right'>

## Privilege Escalation تصعيد الصلاحيات 


### لتحميل بصيغ متعددة تفضل:
- صيغة JSON :[تفضل هنا]() 
- صيغة XLS :[تفضل هنا]()
- صيغة CSV :[تفضل هنا]() 
- صيغة XML :[تفضل هنا]()
- صيغة SQL :[تفضل هنا]()
- صيغة YML :[تفضل هنا]()
 
### التقنيات / Techniques

| ID / المعرف | المعرف الفرعي | الاسم/ Name                                                              |  الوصف / Description |
|-------------|---------------|--------------------------------------------------------------------------|----------------------|
| T1548       |               | اساءة استخدام ميزة رفع الصلاحيات / Abuse Elevation Control Mechanism     |                      |
| T1548       | .001          | Setuid and Setgid                                                        |                      |
| T1548       | .002          | تخطي صلاحيات التحكم بالحسابات / Bypass User Account Control              |                      |
| T1548       | .003          | Sudo and Sudo Caching                                                    |                      |
| T1548       | .004          | Elevated Execution with Prompt                                           |                      |
| T1134       |               | Access Token Manipulation                                                |                      |
| T1134       | .001          | Token Impersonation/Theft                                                |                      |
| T1134       | .002          | Create Process with Token                                                |                      |
| T1134       | .003          | Make and Impersonate Token                                               |                      |
| T1134       | .004          | Parent PID Spoofing                                                      |                      |
| T1134       | .005          | SID-History Injection                                                    |                      |
| T1547       |               | Boot or Logon Autostart Execution                                        |                      |
| T1547       | .001          | Registry Run Keys / Startup Folder                                       |                      |
| T1547       | .002          | Authentication Package                                                   |                      |
| T1547       | .003          | Time Providers                                                           |                      |
| T1547       | .004          | Winlogon Helper DLL                                                      |                      |
| T1547       | .005          | Security Support Provider                                                |                      |
| T1547       | .006          | Kernel Modules and Extensions                                            |                      |
| T1547       | .007          | Re-opened Applications                                                   |                      |
| T1547       | .008          | LSASS Driver                                                             |                      |
| T1547       | .009          | Shortcut Modification                                                    |                      |
| T1547       | .010          | Port Monitors                                                            |                      |
| T1547       | .011          | Plist Modification                                                       |                      |
| T1547       | .012          | Print Processors                                                         |                      |
| T1037       |               | نظام اقلاع او الدخول بواسطة سكربت / Boot or Logon Initialization Scripts |                      |
| T1037       | .001          | سكربت الدخول لنظام ويندوز / Logon Script (Windows)                       |                      |
| T1037       | .002          | سكربت الدخول لنظام ماك Logon Script (Mac)                                |                      |
| T1037       | .003          | سكربت تسجيل الشبكة / Network Logon Script                                |                      |
| T1037       | .004          | Rc.common                                                                |                      |
| T1037       | .005          | Startup Items                                                            |                      |
| T1543       |               | انشاء او تعديل عمليات النظام / Create or Modify System Process           |                      |
| T1543       | .001          | تفعيل البرمجية / Launch Agent                                            |                      |
| T1543       | .002          | Systemd Service                                                          |                      |
| T1543       | .003          | خدمات الويندوز / Windows Service                                         |                      |
| T1543       | .004          | Launch Daemon                                                            |                      |
| T1484       |               | Domain Policy Modification                                               |                      |
| T1484       | .001          | Group Policy Modification                                                |                      |
| T1484       | .002          | Domain Trust Modification                                                |                      |
| T1546       |               | Event Triggered Execution                                                |                      |
| T1546       | .001          | Change Default File Association                                          |                      |
| T1546       | .002          | Screensaver                                                              |                      |
| T1546       | .003          | Windows Management Instrumentation Event Subscription                    |                      |
| T1546       | .004          | .bash_profile and .bashrc                                                |                      |
| T1546       | .005          | Trap                                                                     |                      |
| T1546       | .006          | LC_LOAD_DYLIB Addition                                                   |                      |
| T1546       | .007          | Netsh Helper DLL                                                         |                      |
| T1546       | .008          | Accessibility Features                                                   |                      |
| T1546       | .009          | AppCert DLLs                                                             |                      |
| T1546       | .010          | AppInit DLLs                                                             |                      |
| T1546       | .011          | Application Shimming                                                     |                      |
| T1546       | .012          | Image File Execution Options Injection                                   |                      |
| T1546       | .013          | PowerShell Profile                                                       |                      |
| T1546       | .014          | Emond                                                                    |                      |
| T1546       | .015          | Component Object Model Hijacking                                         |                      |
| T1068       |               | Exploitation for Privilege Escalation                                    |                      |
| T1574       |               | Hijack Execution Flow                                                    |                      |
| T1574       | .001          | DLL Search Order Hijacking                                               |                      |
| T1574       | .002          | DLL Side-Loading                                                         |                      |
| T1574       | .004          | Dylib Hijacking                                                          |                      |
| T1574       | .005          | Executable Installer File Permissions Weakness                           |                      |
| T1574       | .006          | LD_PRELOAD                                                               |                      |
| T1574       | .007          | Path Interception by PATH Environment Variable                           |                      |
| T1574       | .008          | Path Interception by Search Order Hijacking                              |                      |
| T1574       | .009          | Path Interception by Unquoted Path                                       |                      |
| T1574       | .010          | Services File Permissions Weakness                                       |                      |
| T1574       | .011          | Services Registry Permissions Weakness                                   |                      |
| T1574       | .012          | COR_PROFILER                                                             |                      |
| T1055       |               | حقن العمليات / Process Injection                                         |                      |
| T1055       | .001          | Dynamic-link Library Injection                                           |                      |
| T1055       | .002          | حقن البرمجيات الجاهزة للعمل / Portable Executable Injection              |                      |
| T1055       | .003          | Thread Execution Hijacking                                               |                      |
| T1055       | .004          | Asynchronous Procedure Call                                              |                      |
| T1055       | .005          | Thread Local Storage                                                     |                      |
| T1055       | .008          | Ptrace System Calls                                                      |                      |
| T1055       | .009          | Proc Memory                                                              |                      |
| T1055       | .011          | Extra Window Memory Injection                                            |                      |
| T1055       | .012          | Process Hollowing                                                        |                      |
| T1055       | .013          | Process Doppelgänging                                                    |                      |
| T1055       | .014          | VDSO Hijacking                                                           |                      |
| T1053       |               | جدولة الاعمال والمهام / Scheduled Task/Job                               |                      |
| T1053       | .001          | بيئة لينكس / At (Linux)                                                  |                      |
| T1053       | .002          | بيئة ويندوز / At (Windows)                                               |                      |
| T1053       | .003          | Cron                                                                     |                      |
| T1053       | .004          | Launchd                                                                  |                      |
| T1053       | .005          | جدولة الاعمال / Scheduled Task                                           |                      |
| T1053       | .006          | Systemd Timers                                                           |                      |
| T1078       |               | حساب فعال / Valid Accounts                                               |                      |
| T1078       | .001          | حساب افتراضي / Default Accounts                                          |                      |
| T1078       | .002          | حساب مدير النظام / Domain Accounts                                       |                      |
| T1078       | .003          | حساب محلي / Local Accounts                                               |                      |
| T1078       | .004          | حساب الخدمات السحابية / Cloud Accounts                                   |                      |





</div>
