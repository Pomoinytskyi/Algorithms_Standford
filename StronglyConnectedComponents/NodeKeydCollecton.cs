using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace scc
{
	public class NodeKeydCollection : KeyedCollection<int, Node>
	{
		protected override int GetKeyForItem(Node item) => item.Id;
	}
}