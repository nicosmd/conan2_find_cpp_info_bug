# Conan2 find_cpp_info ignores /usr prefix

This repo demonstrates a bug found in conan 2.0.9. `liba_failed` and `liba_success` are basically
the same packages. Both are exporting a `pkg-config file` and trying to deduce a `CppInfo` object
based on the file conent using the helper `find_cpp_info`. The only difference is that `liba_failed` is
using `/usr` as prefix whereas `liba_success` uses `/usr/local`.

When building both packages using

```bash
conan create .
```

you should see for `liba_failed` the output

```bash
liba/1.0.0: ERROR: Lib dir path is empty but is should be /usr/lib
```

 which means, that the `cpp_info.libdirs` attribute is empty. The deduction failed, since `libdirs`
 should contain `/usr/lib`.

 For `liba_success` the output contains

 ```bash
 liba/1.0.0: lib dir path is right!
 ```

 , which means, that the `libdirs` attribute was deduced successful to `/usr/local/lib`.

