Function GetIP() {
    $localhost = Get-NetIPAddress -AddressFamily IPv4

    return $localhost
}

GetIP