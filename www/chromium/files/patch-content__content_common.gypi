--- ./content/content_common.gypi.orig	2014-08-20 21:02:50.000000000 +0200
+++ ./content/content_common.gypi	2014-08-22 15:06:25.000000000 +0200
@@ -598,6 +598,21 @@
         'content.gyp:common_aidl',
       ],
     }],
+    ['os_bsd==1', {
+      'sources!': [
+        'common/sandbox_linux.cc',
+        'common/sandbox_linux.h',
+        'common/sandbox_init_linux.cc',
+        'common/sandbox_seccomp_bpf_linux.cc',
+        'common/sandbox_seccomp_bpf_linux.h',
+        'common/sandbox_linux/bpf_cros_arm_gpu_policy_linux.cc',
+        'common/sandbox_linux/bpf_gpu_policy_linux.cc',
+        'common/sandbox_linux/bpf_ppapi_policy_linux.cc',
+        'common/sandbox_linux/bpf_renderer_policy_linux.cc',
+        'common/sandbox_linux/sandbox_bpf_base_policy_linux.cc',
+        'common/sandbox_linux/sandbox_seccomp_bpf_linux.cc',
+      ],
+    }],
     ['use_pango == 1', {
       'dependencies': [
         '../build/linux/system.gyp:pangocairo',
