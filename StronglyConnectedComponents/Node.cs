using System.Collections.Generic;

namespace scc
{
	public class Node
	{
		private List<Node> next = new List<Node>();
		private List<Node> previous = new List<Node>();

		public int Id { get; set; }
		public bool IsVisited { get; set; }
		public IReadOnlyList<Node> Next => next.AsReadOnly();
		public IReadOnlyList<Node> Previous => previous.AsReadOnly();
		public Node(int id) => Id = id;

		public void AddNextNode(Node nextNode)
		{
			next.Add(nextNode);
		}

		public void AddPreviousNode(Node previousNode)
		{
			previous.Add(previousNode);
		}

		public void Reverse()
		{
			var cache = next;
			next = previous;
			previous = cache;
		}
	}
}