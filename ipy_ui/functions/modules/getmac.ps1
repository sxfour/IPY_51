Function GetMACInfo {
    $host_mac = (Get-WmiObject Win32_NetworkAdapterConfiguration | Where-Object {$_.ipenabled -EQ $true}).Macaddress | select-object -first 1

    return $host_mac
}

GetMACInfo