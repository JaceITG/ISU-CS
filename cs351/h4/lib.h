%define SYS_read	0
%define SYS_write	1
%define SYS_open	2
%define SYS_close	3
%define SYS_exit	60
%define SYS_getrandom	318

; Default file descriptors for stdin, stdout and stderr:
%define STDIN_FILENO	0
%define STDOUT_FILENO	1
%define STDERR_FILENO	2

; Flags used for open() system call:
%define O_ACCMODE       0o003
%define O_RDONLY        0o0
%define O_WRONLY        0o1
%define O_RDWR          0o2
%define O_CREAT         0o100
%define O_EXCL          0o200
%define O_NOCTTY        0o400
%define O_TRUNC         0o1000
%define O_APPEND        0o2000

; Flags used for getrandom() system call
%define GRND_NONBLOCK	0x01
%define GRND_RANDOM	0x02
