#!/usr/bin/env python3
"""Minimal MCP client demo for DouParse (client-side example only).

This file shows how an MCP client talks to the public DouParse MCP endpoint.
It does NOT contain any server-side source code.

Usage:
    python examples/mcp-client.py
    DOUPARSE_API_KEY=dpk_xxx python examples/mcp-client.py "https://v.douyin.com/xxxx/"
"""

import json
import os
import sys
import urllib.request

ENDPOINT = "https://www.qiaiwan.top/mcp/"
API_KEY = os.environ.get("DOUPARSE_API_KEY", "")


def rpc(method: str, params: dict | None = None, req_id: int = 1) -> dict:
    payload = {
        "jsonrpc": "2.0",
        "id": req_id,
        "method": method,
        "params": params or {},
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        body = resp.read().decode("utf-8")
    # Some transports wrap the JSON-RPC response in an SSE "data:" frame.
    if body.startswith("event:") or body.startswith("data:"):
        lines = [ln[5:].strip() for ln in body.splitlines() if ln.startswith("data:")]
        body = lines[-1] if lines else "{}"
    return json.loads(body)


def main() -> None:
    init = rpc(
        "initialize",
        {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "clientInfo": {"name": "douparse-readme-demo", "version": "1.0"},
        },
    )
    print("server:", init.get("result", {}).get("serverInfo"))

    tools = rpc("tools/list", req_id=2).get("result", {}).get("tools", [])
    print("tools:", ", ".join(t["name"] for t in tools))

    if len(sys.argv) > 1:
        if not API_KEY:
            print("Set DOUPARSE_API_KEY before calling parse_video.", file=sys.stderr)
            return
        result = rpc(
            "tools/call",
            {"name": "parse_video", "arguments": {"url": sys.argv[1]}},
            req_id=3,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2)[:2000])


if __name__ == "__main__":
    main()
