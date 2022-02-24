# ACLAnthologyCopyrights
Based on a file name it returns a license of the paper.

```python
import aac
a=aac.ACLCopyrights()
a('P14-1001')         # 'CC-BY-NC-SA 3.0'
a('2021.acl-long.1')  # 'CC-BY 4.0'
```

