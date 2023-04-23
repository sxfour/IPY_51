Function GetIPInfo() {
    $localhost = Get-NetIPAddress -AddressFamily IPv4

    return $localhost
}
