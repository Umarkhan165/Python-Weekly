import subprocess
import datetime, re



def check_website(url) :
    safe_url = re.sub(r'[^\w\-\.]', '_', url.strip()).strip('_')
    safe_url = url
    try:
        result = subprocess.run(["ping" , "-n",'1', url],capture_output=True , text=True, timeout=5)

        if result.returncode == 0:
            status = f"{url} is UP Ping Output is: {result.stdout.strip()}"
        else:
            status = f"{url} us Down , Error : {result.stdout.strip()}"

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{safe_url}.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] {status}\n")

        print(status)

    except subprocess.TimeoutExpired:
        print(f"Timeout while pinging {url}")

        
url = input("Enter the URL of Website (e.g., google.com): ").strip()


if not url:
    print("Error: URL cannot be empty.")
else:
    check_website(url)