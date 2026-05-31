# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the tool

All source lives in `src/`. Run from that directory so local imports resolve:

```bash
cd src
python3 vdeploy.py --hdf test1.hdf --vdf vtest0.vdf --console --log DEBUG
python3 yamo.py test1.hdf   # pretty-print any definition file as JSON
```

There is no build step, test suite, or linter configuration. The only runtime dependency is `pyyaml` (`pip install -r requirements.txt`).

## Definition file system

The core abstraction is a set of YAML definition files that describe infrastructure. `vidl.py` (`vidl()`) concatenates them into a single YAML stream before parsing — this is how YAML anchors defined in a template file (`hvdef.yaml`) can be referenced in a user file (`.hdf`).

| Extension | Purpose | Template schema |
|-----------|---------|-----------------|
| `.hdf` | Hypervisor Definition File | `hvdef.yaml` |
| `.vdf` | VM Definition File | `vmdef.yaml` |
| `.ndf` | Network Definition File | `netdef.yaml` |
| `.ddf` | Deployment Definition File (references the above) | — |
| `.udf` | Universal Definition File (combines all) | — |
| `.rdf` | Redeployment Definition File | — (not yet implemented) |

The schema files (`hvdef.yaml`, `vmdef.yaml`, `netdef.yaml`) are loaded from `./` first, then `/usr/local/share/vdeploy/` — they must be present in whichever directory `vdeploy.py` is run from. Each schema file defines a YAML anchor (`*HVDef`, `*VMDef`) that user definition files merge from using `<< : *AnchorName`.

`vidl()` prepends the relevant schema file before each user file so anchors are in scope. `.ddf` files are loaded as-is (no schema prepended). `.rdf` and `.udf` loading is stubbed (skipped silently).

## Module architecture

```
vdeploy.py          CLI entry point — parses args, calls provisioning then deployment
getopts.py          argparse wrapper; validates file paths and port range
provisioning.py     DDFContext — loads schema YAMLs into self.hvtemplate/vmtemplate/nettemplate;
                    process_ddf_files() calls vidl() to produce self.hdf/vdf/ndf/ddf/rdf/udf dicts
vidl.py             vidl() — concatenates schema + user YAML files and safe_loads the result
deployment.py       Deploy.__init__() — creates Hypervisor managed objects from ctx.hdf,
                    creates VM managed objects from ctx.vdf; contains a live TESTING block
hypervisor.py       Hypervisor base class + hypervisor_factory(); all VM operation methods
                    raise HVUnimplemented — they are the extension points
hyper_esxi.py       Hyper_ESXi(Hypervisor) — ESXi subclass, all methods still stub
mylog.py            logg() convenience wrapper around Python logging; printlog() helper
pexpect.py          Bundled pexpect 2.3 (ported to Python 3); spawn class manages child PTY
pxssh.py            Bundled pxssh (ported to Python 3); pxssh(spawn) handles SSH login/prompt
vdeploy_server.py   Daemon mode stub — Server class logs start but does nothing
yamo.py             Standalone script: YAML → JSON pretty-printer
```

## Key implementation state

- **Working**: CLI parsing, YAML config loading, logging, SSH session establishment (`Hypervisor.ctl_session()` / `sendcmd()`), hypervisor factory pattern.
- **Stubs**: Every VM operation (`vm_start`, `vm_stop`, `vm_deploy`, etc.) raises `HVUnimplemented`. Only `Hyper_ESXi` exists as a subclass. Daemon mode (`vdeploy_server.Server`) is empty. `.rdf`/`.udf` processing is skipped.
- **TESTING block**: `deployment.py` Deploy.__init__() contains a live block that opens an SSH session and runs `ls -l` on the first hypervisor. It guards with `if hvlist and hvlist[0] is not None`.

## Extending hypervisor support

To add a new hypervisor type:
1. Subclass `Hypervisor` (see `hyper_esxi.py` as the pattern).
2. Override the VM operation methods defined in `hypervisor.py`.
3. Register the new type in `hypervisor_factory()` in `hypervisor.py`.
4. Add the corresponding `HVType` string to the `.hdf` schema.

## SSH / pexpect notes

`pexpect.py` and `pxssh.py` are vendored copies (originally v2.3, 2007), ported to Python 3. They are **not** the PyPI `pexpect` package. The spawn class uses `self.encoding = 'utf-8'` and decodes all child output to `str`; logfiles must be opened in text mode (or will fall back via `_log_write()`). `hypervisor.py` uses `pxssh.pxssh` directly for SSH sessions to hypervisors.
