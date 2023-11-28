I apologize for any confusion. The `lvextend` command is typically used with logical volumes managed by LVM. If your `/dev/vda2` is not part of an LVM setup, we need to take a different approach.

If you want to use the entire unallocated space on `/dev/vdb1` to extend `/dev/vda2`, you would need to follow these general steps:

1. Backup your important data.
2. Create a partition on `/dev/vdb` using a tool like `fdisk` or `parted`.
3. Create a filesystem on the new partition: `mkfs.ext4 /dev/vdb1` (or another filesystem type depending on your preference).
4. Mount the new filesystem: `mount /dev/vdb1 /mnt` (or another mount point).
5. Copy the contents of `/dev/vda2` to `/mnt`.
6. Update the `/etc/fstab` file with the new partition information.
7. Reboot to apply the changes.