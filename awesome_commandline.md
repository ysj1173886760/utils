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