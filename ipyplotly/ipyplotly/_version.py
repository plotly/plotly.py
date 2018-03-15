version_info = (0, 1, 0, 'alpha', 2)

_specifier_ = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc', 'final': ''}

__version__ = '%s.%s.%s%s'%(version_info[0], version_info[1], version_info[2],
  '' if version_info[3]=='final' else _specifier_[version_info[3]]+str(version_info[4]))
