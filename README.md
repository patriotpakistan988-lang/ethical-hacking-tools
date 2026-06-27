# Ethical Hacking Tools

Mobile penetration testing toolkit running on Android via Kali NetHunter (Rootless)

## Device Setup
- Device: Android (Vivo V2342)
- Environment: Termux + Kali NetHunter Rootless
- OS: Kali Linux (proot)
- Arch: ARM64

## Tools Installed

| Tool | Status |
|------|--------|
| Kali NetHunter + VNC GUI | Working |
| Nmap | Working |
| Hydra | Working |
| SQLmap | Working |
| Metasploit | Working |
| Wireshark | Working |
| John the Ripper | Working |
| Aircrack-ng | Working |
| Ghidra | Working |
| Radare2 | Working |
| apktool + JADX | Working |
| Nuclei + Subfinder | Working |
| Wordlists (5.2M+) | Working |
| Java OpenJDK 17 | Working |
## Recent Scan Results

### Nuclei Scan - google.com (Practice)
- Date: 2026-06-28
- Tool: Nuclei v3.8.0
- Templates: 5025 loaded
- Findings: 35 matches (info level)

| Finding | Type | Severity |
|---------|------|----------|
| deprecated-tls (TLS 1.0/1.1) | ssl | info |
| missing-sri | http | info |
| security-txt detected | http | info |
| spf-record-detect | dns | info |
| dmarc-detect | dns | info |
| ssl-dns-names | ssl | info |
| rdap-whois info | http | info |

> Note: Educational practice only. Not a bug bounty target.
## Disclaimer
Educational purposes only. Use on authorized systems only.

## Author
patriotpakistan988-lang | Learning ethical hacking
