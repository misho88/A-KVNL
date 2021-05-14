# A/KVNL
Annotations/KVNL implements annotation support over KVNL

In short, KVNL (Keys, Values and New Lines) is a protocol which accepts data
as a sequence of lines of three possible forms:

```
\n
<key>=<value with no \n in it>\n
<key>:<size>=<arbitrary value>\n
```

Annotations formalize a way to add some arbitrary metadata to the key field,
which is done by including a `!` character. Everything in the key after the
first `!` character is an annotation, which can generally be any text, i.e.,
`<key>` as defined above can be of one of the forms:

```
<key>
<key>!<annotation>
```

## Default Type Annotations

Certain (case-sensitive) annotations are expected to be interpreted as
follows:

- `Int` or `I` for an integer
- `Float` or `F` for a floating-point value
- `Unicode` or `U` for Unicode text
- `ASCII` or `A` for ASCII text
- `Time` or `T` for ISO-formatted time (and date) data


# Usage

The reference implementation here relies on the `kvnl` module (https://github.com/misho88/kvnl).

Decoding:

```
>>> data = b'x!I=1\ny!F=3.14\n\n'
>>> print(data.decode(), end='')
x!I=1
y!F=3.14

>>> from kvnl import loads_block
>>> print(*loads_block(data))
('x!I', b'1') ('y!F', b'3.14')
>>> from a_kvnl import decode_block
>>> print(*decode_block(loads_block(data)))
('x', 1) ('y', 3.14)
```

Encoding:

```
>>> items = [ ('x', 1), ('y', 3.14) ]
>>> from a_kvnl import encode_block
>>> print(*encode_block(items))
('x!I', b'1') ('y!F', b'3.14')
>>> from kvnl import dumps_block
>>> print(dumps_block(encode_block(items)).decode(), end='')
x!I=1
y!F=3.14
```
