# Set the path for the output CSV file
$outputFile = "C:\Scripts\ForwardingUsers.csv"

# Connect to Exchange
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://<SERVER>/PowerShell/ -Authentication Kerberos
Import-PSSession $Session

# Get all mailbox users in the Exchange organization
$mailboxes = Get-Mailbox -ResultSize Unlimited

# Create an empty array to store the results
$results = @()

# Loop through each mailbox and check for email forwarding rules
foreach ($mailbox in $mailboxes) {
    $userName = $mailbox.UserPrincipalName
    $forwardingRules = Get-InboxRule -Mailbox $userName | Where-Object {$_.ForwardTo -ne $null -or $_.RedirectTo -ne $null}
    
    # If forwarding rules are found, add the mailbox user to the results array
    if ($forwardingRules) {
        $result = New-Object PSObject -Property @{
            User = $userName
        }
        $results += $result
    }
}

# Export the results array to a CSV file
$results | Export-Csv -Path $outputFile -NoTypeInformation

# Disconnect from Exchange
Remove-PSSession $Session
