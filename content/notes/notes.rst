NOT FOR USE
===========

host1:# netstat -ng | grep ${MULTICAST}
host1:# tcpdump -i ${interface} host ${MULTICAST} -w dump.pcap
host1:# tcpreplay --stats=1 -i enp1s0 dump.pcap

host2:$ vlc [udp|rtp]://@${MULTICAST}:${MULTICAST_PORT} --novideo
host2:$ ffplay -nodisp -noaudio [udp|rtp]://@${MULTICAST}:${MULTICAST_PORT}


Build java jar file from on android 7.0
=======================================
Add do Android.mk: 'LOCAL_JACK_ENABLED := disabled'


Fix nginx exscessive disk usage
===============================

Add to /etc/nginx.conf:
http {
...
proxy_cache_path /dev/null use_temp_path=off keys_zone=null:1m;
...
}
