Write-Host "Escaneo red"
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)

$rango_ip = @(1..255)

function red-a {
foreach ( $r in $rango_ip )
    {
        $actual = $rango + $r 
        $responde = Test-Connection $actual -Quiet -Count 1 
        if ( $responde -eq "True" )
        {
            Write-Host "Puerto activo: " -NoNewline; Write-Host $actual -ForegroundColor Green
        }
    }
    }

red-a