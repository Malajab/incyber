# Prompt the user for the Exchange server name, output folder path, and zip file name
$server = Read-Host "Enter the Exchange server name or IP address"
$outputFolder = Read-Host "Enter the output folder path (e.g. C:\Scripts\Attachments)"
$zipFileName = Read-Host "Enter the name of the zip file to create (e.g. Attachments.zip)"

# Connect to Exchange
Write-Host "Connecting to Exchange..." -ForegroundColor Yellow
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri "http://$server/PowerShell/" -Authentication Kerberos
Import-PSSession $Session

# Search for emails with attachments that contain macros
$attachments = Get-Mailbox -ResultSize Unlimited | Search-Mailbox -SearchQuery 'hasattachment:true AND attachment:microsoft.office*' -TargetMailbox "DiscoveryMailbox" -TargetFolder "TempExport" -EstimateResultOnly:$false -LogLevel Full

# Loop through each attachment and save it to the output folder
foreach ($attachment in $attachments) {
    $attachmentPath = "$outputFolder\$($attachment.FileName)"
    $attachment.Content | Set-Content -Path $attachmentPath -Encoding Byte
}

# Compress the output folder to a zip file
$zipFilePath = "$outputFolder\$zipFileName"
Compress-Archive -Path $outputFolder\* -DestinationPath $zipFilePath -Force

# Disconnect from Exchange
Write-Host "Disconnecting from Exchange..." -ForegroundColor Yellow
Remove-PSSession $Session

# Display a message when the script has completed
Write-Host "Done! The attachments have been saved to $zipFilePath" -ForegroundColor Green
