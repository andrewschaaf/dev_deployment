
# Overview

A Django project to run an arbitrary Django app.

## Varnish

<pre>sudo varnishd -F -a :80 -T localhost:6085 -f conf/varnish.conf -s file,`pwd`/tmpdir/varnish.cache,10M</pre>

## Tokyo Tyrant
<pre>ttserver -port 7000 tmpdir/tyrant.tcb#opts=ld</pre>

## Redis
<pre>redis-server conf/redis.conf</pre>

## Django
<pre>python manage.py runserver</pre>
<pre>python manage.py runserver -H `internal-ip`</pre>



