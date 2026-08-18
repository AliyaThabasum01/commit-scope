import subprocess


def run_git(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


print("=" * 45)
print("🔎 CommitScope")
print("=" * 45)

branch = run_git(["git", "branch", "--show-current"])
status = run_git(["git", "status", "--short"])

print(f"\n🌿 Branch: {branch or 'Unknown'}")

if not status:
    print("\n✅ Working tree is clean.")
else:
    lines = status.splitlines()

    modified = sum(1 for line in lines if line.startswith(" M"))
    added = sum(1 for line in lines if line.startswith("A "))
    deleted = sum(1 for line in lines if line.startswith(" D"))

    print(f"\n📊 Changes: {len(lines)}")
    print(f"📝 Modified: {modified}")
    print(f"➕ Added: {added}")
    print(f"➖ Deleted: {deleted}")

    print("\nFiles:")
    for line in lines:
        print(f"  {line}")
