time:

```shell
watch -t -n 1 "date +%T|figlet -f big"
```

rolling screen:

```shell
cat /dev/urandom | hexdump -C | grep "ca fe"
```

simulate typing:

```shell
echo "simulate on-screen typing" | pv -qL 10
```

execute command on specified time:

```shell
echo "ls -l" | at midnight
```

check md5sum using re-direct

it will output something if there has difference. And output nothing if they are same.

you can also use "echo $!" to check the result, 0 means there is no error

```shell
diff <(md5sum musicbrainz-cmudb2020.db.gz) <(echo "a80fe4365a228d4096225068801771f8  musicbrainz-cmudb2020.db.gz")

# basic pattern
diff <(md5sum <your-file-name>) <(echo "checksum filename")
```

check lib version

```shell
dpkg -l | grep <lib-name>
```

clean cache

```shell
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
```

terminal countdown timer

```shell
countdown=3600 date1=$((`date +%s` + ${countdown})) watch -tpn1 'echo FOCUSING $(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S) | figlet -f big'
```

remote file copy / ssh cp

scp -r (recursive, directory only) -P (Caps specified port) username@hostname:/path/to/your/remote/file /path/to/save

```shell
scp -r -P 20231 root@120.236.247.203:/opt/code_chap_2_3/pycnml /home/sheep
```