import speedtest

test = speedtest.Speedtest()

print("Loading server list")
test.get_servers()
print("Choosing best server")
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")

print("Performing download test...")
download_test = test.download();
print("Performing upload test...")
upload_test = test.download();
ping_result = test.results.ping

print(f"Download speed: {download_test / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_test / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {download_test:.2f}ms")

