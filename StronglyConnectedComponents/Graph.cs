using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace scc
{
	public class Graph
	{
		private NodeKeydCollection graph = new NodeKeydCollection();

		public static Graph ReadFromFile(string fileName)
		{
			Graph result = new Graph();
			using (FileStream fileStream = File.Open(fileName, FileMode.Open))
			using (StreamReader streamReader = new StreamReader(fileStream))
			{
				string line;
				int beginNodeId, endNodeId;
				while ((line = streamReader.ReadLine()) != null)
				{
					var numbers = line.Split(" ");
					beginNodeId = int.Parse(numbers[0]);
					endNodeId = int.Parse(numbers[1]);
					result.AddDirectedEdge(beginNodeId, endNodeId);
				}
			}

			return result;
		}

		public void AddDirectedEdge(int beginNodeId, int endNodeId)
		{
			var beginNode = GetOrCreateNode(beginNodeId);
			var endNode = GetOrCreateNode(endNodeId);

			beginNode.AddNextNode(endNode);
			endNode.AddPreviousNode(beginNode);
		}

		private Node GetOrCreateNode(int nodeId)
		{
			Node node;
			if (!graph.Contains(nodeId))
			{
				node = new Node(nodeId);
				graph.Add(node);
			}
			else
			{
				node = graph[nodeId];
			}
			return node;
		}

		public void Reverse()
		{
			foreach (Node node in graph)
			{
				node.Reverse();
			}
		}

		public void Print(string prefix)
		{
			System.Console.WriteLine(prefix);
			if (graph.Count > 20)
			{
				System.Console.WriteLine($"Graph too big. {graph.Count} nodes");
				return;
			}

			foreach (Node node in graph)
			{
				System.Console.WriteLine($"{node.Id} -> {string.Join(", ", node.Next.Select(n => n.Id.ToString()))}");
			}
		}

		public (List<Node> order, Dictionary<Node, int> clusters) GetNodeOrdered(List<Node> inputOrder = null)
		{
			if (inputOrder == null)
			{
				inputOrder = graph.ToList();
			}

			var order = new List<Node>();
			var clusters = new Dictionary<Node, int>();
			foreach (Node node in inputOrder)
			{
				if (node.IsVisited)
				{
					continue;
				}

				Stack<Node> stack = new Stack<Node>();
				int clusterSize = 1;

				stack.Push(node);

				while (stack.Any())
				{
					var current = stack.Peek();
					if (current.IsVisited)
					{
						order.Add(current);
						stack.Pop();
						clusterSize++;
					}
					else
					{
						current.IsVisited = true;
						foreach (Node next in current.Next.Where(n => !n.IsVisited))
						{
							if (!stack.Contains(next)) //ToDo: improve performance
							{
								stack.Push(next);
							}
						}
					}
				}

				clusters.Add(node, clusterSize);
			}

			return (order, clusters);
		}

		public void ResetIsVited(bool newValue)
		{
			foreach (Node node in graph)
			{
				node.IsVisited = newValue;
			}
		}
	}
}