"""Decode a Nuxt 3 __NUXT_DATA__ (devalue) payload into plain Python data."""
import json, re

def decode(arr):
    memo = {}
    def get(i):
        if isinstance(i, int) and i < 0:
            return None
        if i in memo:
            return memo[i]
        v = arr[i]
        if isinstance(v, list):
            if v and isinstance(v[0], str) and v[0] in ('ShallowReactive', 'Reactive', 'Ref', 'ShallowRef', 'EmptyRef', 'EmptyShallowRef'):
                r = get(v[1]) if len(v) > 1 else None
                memo[i] = r
                return r
            if v and isinstance(v[0], str) and v[0] in ('Set', 'Map', 'Date', 'BigInt', 'undefined', 'NuxtError'):
                memo[i] = v
                return v
            out = []
            memo[i] = out
            out.extend(get(x) for x in v)
            return out
        if isinstance(v, dict):
            out = {}
            memo[i] = out
            for k, x in v.items():
                out[k] = get(x)
            return out
        memo[i] = v
        return v
    return get(0)

def from_html(html):
    m = re.search(r'<script type="application/json"[^>]*id="__NUXT_DATA__">(.*?)</script>', html, re.S)
    return decode(json.loads(m.group(1)))
