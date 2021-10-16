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

清除缓存

```shell
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
```